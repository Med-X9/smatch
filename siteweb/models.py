from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Projet(models.Model):
    
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projets_images/')
    date_de_creation = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=255)
    categorie = models.CharField(max_length=50, choices=[('webApp', 'Web Application'), ('mobileApp', 'Mobile Application'), ('programation4.0', 'Programmation 4.0')])
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
    def get_absolute_url(self):
        return reverse("detail_projet", kwargs={"slug": self.slug})
