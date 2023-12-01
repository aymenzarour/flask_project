# flask_project
This project demonstrates a simple Flask web application that includes an input form. Users can enter text through the form, which is then displayed on the page. The project is designed to be containerized using Docker.

## Project Structure
.

- **`app.py`**: The main Python script containing the Flask application. It defines two routes - the root route (`/`) with a welcome message and an input form route (`/input`) to handle user input.

- **`Dockerfile`**: The Docker configuration file specifying the base image, working directory, and necessary steps to build the Docker image. It includes the installation of Flask and exposes port 5000 for the application.

- **`templates/input_form.html`**: HTML template for the input form. It includes a simple form with a text input field and a submit button.

## How to Run

1. Ensure you have Docker installed on your system.

2. Build the Docker image:

   ```bash
   docker build -t flask-app .
   
3. Run the Docker container:
   
   ```bash
   docker run -p 5000:5000 flask-app

4. Access the application in your web browser at http://localhost:5000/input. 


## Usage

- Visit the input form page.
- Enter text in the input field.
- Click the "Submit" button.
- The entered text will be displayed on the page.
   
## Notes

- This is a basic example meant for educational purposes.
