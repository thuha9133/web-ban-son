from django.db import models

class Image(models.Model):
    file = models.ImageField(upload_to='img_uploads/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or str(self.file)
