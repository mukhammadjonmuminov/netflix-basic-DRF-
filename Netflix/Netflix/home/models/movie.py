from django.db import models
from .actor import Actor

class Movie(models.Model):
    name = models.CharField(max_length=150, blank=False, null=True)
    year = models.DateField()
    imdb = models.IntegerField()
    roles = (
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Epics', 'Epics'),
        ('Serial', 'Serial'),
        ('Documentary', 'Documentary'),
        ('Dedective', 'Dedective'),
        ('Fantastic', 'Fantastic'),
        ('Scientific', 'Scientific'),
        ('Artistic', 'Artistic'),
        ('Historical', 'Historical'),
    )

    genre = models.CharField(max_length=150, choices=roles)
    actor = models.ManyToManyField(Actor)
    watched = models.IntegerField(default=0)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

