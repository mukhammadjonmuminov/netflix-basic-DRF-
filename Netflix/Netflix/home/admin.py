from django.contrib import admin
from .models.actor import Actor
from .models.movie import Movie
from .models.comment import Comment

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Comment)
