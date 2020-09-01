from django.db import models

# Create your models here.
class Redirect(models.Model):
    original_url = models.URLField(max_length=500)
    slug = models.CharField(max_length=5, null=False, blank=True, unique=True)

    def __str__(self):
        return str(self.id) + ' ' + self.original_url + ' ' + self.slug