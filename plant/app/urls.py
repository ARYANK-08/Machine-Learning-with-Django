# your_app/urls.py
from django.urls import path
from .views import upload_image

app_name = 'your_app'

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    # Add other URL patterns as needed
]
