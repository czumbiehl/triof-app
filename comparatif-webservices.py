# Creating a summary table for the comparison of cloud services based on vision AI capabilities, pricing, and performance.
import pandas as pd

# Define the data
data = {
    'Service': ['Google Cloud Vision AI', 'Amazon Rekognition', 'IBM Watson Visual Recognition', 'OVHcloud AI Training'],
    'Provider': ['Google', 'Amazon', 'IBM', 'OVHcloud'],
    'Functionality': [
        'Object detection, image labeling, face detection, OCR, explicit content detection',
        'Object detection, image and video analysis, face comparison, text detection, unsafe content detection',
        'Image classification, face detection, explicit content detection',
        'Custom machine learning model training and deployment, not specific to vision but applicable'
    ],
    'Pricing Model': [
        'Per image/request, tiered pricing based on volume',
        'Per image/minute of video processed, tiered pricing based on volume',
        'Per image/request, tiered pricing; free tier available',
        'Based on the computational resources used (CPU, GPU, RAM, etc.)'
    ],
    'Use Case Speed': [
        'High, real-time analysis possible',
        'High, real-time analysis possible for images, near-real-time for videos',
        'Moderate to high, depending on the complexity of the analysis',
        'Depends on the specific machine learning model and resources allocated'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
print(df)
