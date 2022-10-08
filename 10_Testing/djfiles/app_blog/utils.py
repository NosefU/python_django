import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class GetUUIDName:
    def __init__(self, path: str):
        self.path = path

    def __call__(self, _, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(self.path, filename)
