from django.db import models
from django.core.validators import MinValueValidator

# Новость в списке
class New(models.Model):
    title = models.CharField(
        max_length=128,
        unique=True,  # названия новостей не должны повторяться
    )
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
    )
    # поле категории будет ссылаться на модель категории
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='news', # все новости в категории будут доступны через поле news
    )

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'


# Категория, к которой будет привязываться товар
class Author(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

