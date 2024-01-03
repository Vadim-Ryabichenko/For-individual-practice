from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} | {self.age}'  
    

class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'