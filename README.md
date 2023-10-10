# URL-Shortener-Service

The URL shortener service allows users to shorten long URLs into unique, shortened URLs. When users access the shortened URL, they are redirected to the original long URL. Users can view the list of original long URLs and unique, shortened URLs.

# Set Up the Environment 

To set up the environment to run the Flask application, follow these steps: 
1. Ensure you have Python installed on your machine. It can be downloaded from the Python website (https://www.python.org/downloads/).

2. Install Flask and the required dependencies: <br>

    ``` pip install Flask flask_sqlalchemy ```

3. Clone the GitHub repository to your local machine: <br>

    ``` git clone https://github.com/yourusername/repo-name.git ``` <br>
    
   Navigate to the project folder: <br>
   
   ``` cd repo-name ```

4. Set Up Virtual Environment: <be>

   ``` python -m venv venv ```  <br>
   
   ``` source venv/bin/activate (On Mac)  ``` <br>
   ``` venv\Scripts\activate (On Windows) ``` <br>

5. Install Python Dependencies: <be>

   ``` pip install -r requirements.txt ```

6. Run the Application: <br>

   ``` python app.py  ``` <br>
   
   The application can be accessed in the terminal, or open your web browser and go to http://localhost:5000 to access the URL Shortener application.

# URL Shortening Algorithm 

First, the entered URL is checked if it is valid using regular expression validation. <br>
The algorithm uses a combination of a secure hash function (SHA-256) and random characters to generate unique shortened URLs. This approach makes it highly unlikely for two different long URLs to produce the same short URL. SHA-256 is a secure hashing algorithm, making it challenging for attackers to reverse-engineer the original URL from the short URL. The use of random characters in the short URL further reduces the likelihood of collisions.


# Project Structure

* app.py: The main Flask application file that defines the routes and handles URL shortening, redirection, and listing.
  
* templates: Directory containing HTML templates for the web pages. 
    * index.html: The home page for entering long URLs and displaying shortened URLs. 
    * list_urls.html: The page for listing all original and shortened URLs. 

* static: Directory containing static files such as CSS and Script.js.
  
* Instance
    *urls.db: SQLite database file to store URL mappings.
  
* requirements.txt: List of Python packages required for the project.
  
* README.md: This README file. 

