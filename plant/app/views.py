from django.shortcuts import render
from .forms import ImageUploadForm
from .ml_model import plant_recognition_model

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form to get the uploaded image instance
            uploaded_image = form.save(commit=False)

            # Pass the image URL to the recognition model
            result = plant_recognition_model(uploaded_image.image)

            return render(request, 'result.html', {'result': result, 'uploaded_image': uploaded_image.image.url})
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})
