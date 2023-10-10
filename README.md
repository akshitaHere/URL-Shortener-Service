# URL-Shortener-Service

The URL shortener service allows users to shorten long URLs into unique, shortened URLs. When users access the shortened URL, they are redirected to the original long URL. Users can view the list of original long URLs and unique, shortened URLs.

# Set Up the Environment 

To set up the environment to run the Flask application, follow these steps: 
1. Ensure you have Python installed on your machine. You can download it from the Python website (https://www.python.org/downloads/).

2. Install Flask and the required dependencies: <br>
    ``` pip install Flask flask_sqlalchemy ```

3. Clone your GitHub repository to your local machine: <br>
    ``` git clone https://github.com/yourusername/repo-name.git ``` <br>
   Navigate to the project folder: <br>
   ``` cd repo-name ```

4. Set Up Virtual Environment (Optional but recommended): <br>
   ``` python -m venv venv ```  <br>
   ``` source venv/bin/activate (On Mac)  ``` <br>
   ``` venv\Scripts\activate (On Windows) ``` <br>

5. Install Python Dependencies: <br>
   ``` pip install -r requirements.txt ```

6. Run the Application: <br>
   ``` python app.py  ``` <br>
   Open your web browser and go to http://localhost:5000 to access the URL Shortener application.
