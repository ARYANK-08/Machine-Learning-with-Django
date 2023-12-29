# ml_model.py
import cv2
from keras.models import load_model
import numpy as np

# Load the pre-trained model
model = load_model('C:\\Users\\kyath\\OneDrive\\Desktop\\plantrecognition\\plant_recognition_model.h5')
print(model)
def plant_recognition_model(image_instance):
    img = cv2.imdecode(np.frombuffer(image_instance.read(), np.uint8), cv2.IMREAD_COLOR)
    resized_img = cv2.resize(img, (331, 331)).reshape(-1, 331, 331, 3) / 255.0
    prediction = model.predict(resized_img)
    class_names = ['Karanj Trunk', 'Karanj Leaf', 'Karanj Seed', 'Neem Trunk', 'Neem Leaf', 'Neem Seed', 'Peeple Trunk', 'Peeple Leaf', 'Peeple Seed']
    class_prediction = class_names[np.argmax(prediction)]
    
    if class_prediction in ['Karanj Trunk', 'Karanj Leaf', 'Karanj Seed']:
        output_text = 'Karanj: Popularly known as Indian Beech in outside India is a medicinal herb used mainly for skin disorders. Karanja oil is applied to the skin to manage boils, rashes, and eczema as well as heal wounds due to its antimicrobial properties. The oil can also be useful in arthritis due to its anti-inflammatory activities.'
    elif class_prediction in ['Neem Trunk', 'Neem Leaf', 'Neem Seed']:
        output_text = 'Neem: A versatile medicinal tree. Neem oil and neem leaves are used for various medicinal purposes. It has anti-inflammatory, antifungal, and antibacterial properties, making it beneficial for skin care, hair care, and managing various health conditions.'
    elif class_prediction in ['Peeple Trunk', 'Peeple Leaf', 'Peeple Seed']:
        output_text = 'Peepal: The bark of the Peepal tree, rich in vitamin K, is an effective complexion corrector and preserver. It also helps in various ailments such as strengthening blood capillaries, minimizing inflammation, healing skin bruises faster, increasing skin resilience, treating pigmentation issues, wrinkles, dark circles, lightening surgery marks, scars, and stretch marks.'
    else:
        output_text = 'Unknown Plant'

    return class_prediction, output_text
