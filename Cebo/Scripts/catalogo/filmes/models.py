from django.db import models

# Create your models here.
class Filmes(models.Model):
    Name = models.CharField(max_length=70),
    Details = models.TextField(),
    Year = models.IntegerField(),
    Gender = models.CharField(max_length=100),
    Image = models.TimeField();
    
    def __str__(self):
        return self.titulo