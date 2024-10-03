from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
import os
# Create your models here.

def validate_image_or_svg(value):
    ext = os.path.splitext(value.name)[1].lower()  
    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']  

    if ext == '.svg':  
        if not value.file.readable():
            raise ValidationError('The uploaded SVG file is corrupted.')
    elif ext in valid_image_extensions:  # For raster images, validate using Pillow
        try:
            img = Image.open(value)
            img.verify()  # Verifies that the image can be opened and is not corrupted
        except (IOError, SyntaxError):
            raise ValidationError('Upload a valid image. The file you uploaded was either not an image or a corrupted image.')
    elif ext == '.json':  # For Lottie files, validate if it's a valid JSON
        try:
            import json
            json_content = value.read().decode('utf-8')
            json.loads(json_content)  # This ensures it's a valid JSON
        except (ValueError, UnicodeDecodeError):
            raise ValidationError('The uploaded Lottie file is invalid or corrupted.')
    else:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are {valid_image_extensions + [".svg"]}')


class ImageModel(models.Model):
    title = models.CharField(max_length=100) 
    image = models.FileField(upload_to='images/', validators=[validate_image_or_svg]) 

    def __str__(self):
        return self.title
