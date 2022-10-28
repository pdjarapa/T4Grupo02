from django.db import models

# Create your models here.
class Recurso(models.Model):
    title = models.CharField(max_length=50)
    title_minimo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Sesion(Recurso):
    description = models.TextField()

    def __str__(self):
        """
        """
        return "Video: %s - %s " % (self.title, self.title_minimo)

class Tutoria(Recurso):
    markdown_content = models.TextField()

    def __str__(self):
        """
        """
        return "Video: %s - %s " % (self.title, self.title_minimo)