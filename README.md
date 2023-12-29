Download ML model from here : https://drive.google.com/file/d/1kb1w4xShRynP30C38QQw8FFpkqGZtJSl/view?usp=sharing

# Leaf Detector ML Model

Leaf Detector ML Model is a Django web application that takes input images of leaves, processes them using a machine learning model, and provides the output of the detected plant.
```markdown


## Prerequisites

1. Python Virtual Environment:
   ```bash
   python -m venv venv
   ```

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note:** Ensure that your `pip` is upgraded to the latest version.

## Database Setup

1. Apply Migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the Leaf Detector web application.

## Usage

1. Upload an image of a leaf using the web interface.
2. The application processes the image using the machine learning model.
3. View the result page to see the detected plant and additional information.

## Additional Notes

- Make sure to have a working internet connection for the machine learning model to function properly.

- Customize the web interface and styles according to your preferences in the Django templates and CSS files.

- For production deployment, consider updating Django settings (e.g., `DEBUG`, `ALLOWED_HOSTS`) and use a production-ready web server.

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace the placeholder text and URLs with the actual details relevant to your project. Additionally, include a `LICENSE` file with the text of the MIT License in your repository.
