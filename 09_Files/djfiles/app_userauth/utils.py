import os

from django.utils.deconstruct import deconstructible


@deconstructible
class GetUserDirectory:
    def __init__(self, path: str):
        self.path = path

    def __call__(self, instance, filename):
        filename = str(instance.user.id) + "_" + filename
        return os.path.join(self.path, str(instance.user.id), filename)


@deconstructible
class GetPostDirectory:
    def __init__(self, path: str):
        self.path = path

    def __call__(self, instance, filename):
        filename = str(instance.record_id) + "_" + filename
        return os.path.join(self.path, str(instance.record_id), filename)
