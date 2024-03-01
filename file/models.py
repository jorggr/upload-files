from django.db import models

# Create your models here.


class FileData(models.Model):
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.uploaded_at)
