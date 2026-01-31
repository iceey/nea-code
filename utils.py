"""
Image preprocessing function to avoid repeating code.
"""

from PIL import Image
import numpy as np


# ============================================================================
# IMAGE PREPROCESSING
# ============================================================================

def preprocess_image(image):
    """
    Convert uploaded image so the model can use it.
    Makes it greyscale, resizes to 28x28, and normalises to 0-1.
    """
    # Handle both numpy arrays and PIL images
    if isinstance(image, np.ndarray):
        if len(image.shape) == 3:
            img = Image.fromarray(image.astype('uint8'))
        else:
            img = Image.fromarray(image.astype('uint8'))
    else:
        img = image
    
    img = img.convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img).astype('float32') / 255.0
    
    return img_array
