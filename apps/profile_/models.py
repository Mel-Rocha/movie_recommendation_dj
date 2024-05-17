from uuid import uuid4

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class MovieGenre(models.TextChoices):
    ACTION = 'AC', 'Action'
    ADVENTURE = 'AD', 'Adventure'
    COMEDY = 'CO', 'Comedy'
    DRAMA = 'DR', 'Drama'
    FANTASY = 'FA', 'Fantasy'
    HORROR = 'HO', 'Horror'
    MYSTERY = 'MY', 'Mystery'
    ROMANCE = 'RO', 'Romance'
    SCIFI = 'SC', 'Sci-Fi'
    THRILLER = 'TH', 'Thriller'


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    favorite_genre = models.CharField(
    max_length=2,
    choices=MovieGenre.choices,
    default=MovieGenre.ROMANCE,
)