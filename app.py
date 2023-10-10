from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10), unique=True)

    def __init__(self, long, short):  
        self.long = long
        self.short = short


with app.app_context():
    db.create_all()


def shorten_url(long_url, length=6, max_attempts=10):
    attempts = 0
    while attempts < max_attempts:
        # Hash the long URL using a secure hash function (SHA-256)
        sha256_hash = hashlib.sha256(long_url.encode()).hexdigest()
        short_url = ''.join(random.choice(sha256_hash) for _ in range(length))

        # Check if the generated short code already exists
        existing_url = Urls.query.filter_by(short=short_url).first()
        if not existing_url:
            return short_url
        attempts += 1
            
    raise Exception("Failed to generate a unique short URL after multiple attempts")


@app.route('/', methods=['POST', 'GET'])
def home():
    try:
        if request.method == "POST":
            url_received = request.form["nm"]
            #check if URL already in db
            found_url = Urls.query.filter_by(long=url_received).first()
            if found_url:
                #return short url if found
                return found_url.short
            else:
                #create short url if not found
                short_url = shorten_url(url_received)
                new_url = Urls(url_received, short_url)
                db.session.add(new_url)
                db.session.commit()
                return short_url
        else:
            return render_template("index.html")
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


@app.route('/<short_url>')
def redirection(short_url):
    try:
        long_url = Urls.query.filter_by(short=short_url).first()
        if long_url:
            return redirect(long_url.long)
        else:
            return "URL does not exist", 404
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


@app.route('/list')
def list_urls():
    try:
        urls = Urls.query.all()
        base_url = request.url_root

        url_list = [{'original_url': url.long, 'full_shortened_url': f"{base_url}{url.short}"} for url in urls]

        return render_template("list_urls.html", urls=url_list)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
