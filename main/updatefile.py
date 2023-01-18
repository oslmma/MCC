import os

from django.conf import settings


def update(f, name, family):
    namefamily = name + ' ' + family
    path = os.path.join(settings.MEDIA_ROOT, "uploads", namefamily)
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path, f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
