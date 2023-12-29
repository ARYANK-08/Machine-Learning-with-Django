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

## Website Images : 

![image](https://github.com/ARYANK-08/Machine-Learning-with-Django/assets/120780784/62a11871-3b7e-4047-92da-ed0a463221f3)
![image](https://github.com/ARYANK-08/Machine-Learning-with-Django/assets/120780784/1d8d62a7-bb31-4373-a059-010ca0a537a7)


