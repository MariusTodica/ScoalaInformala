
import os
from django.conf import settings


def store_uploaded_file(file):

    destination_dir = os.path.join(settings.MEDIA_ROOT, 'images')
    os.makedirs(destination_dir, exist_ok=True)

    with open(os.path.join(destination_dir, file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
