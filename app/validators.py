import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() == '.mp4':
        raise ValidationError('Unsupported file extension.')