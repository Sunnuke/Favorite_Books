from django.db import models
from app_LR.models import User
# Create your models here.
class BookManager(models.Manager):
    def valid_book(self, postData):
        errors ={}
        # Checking length of title
        if postData['title'] < 2:
            errors['title'] = "The title of the book should be at least 2 characters!"
        # Checking length of description
        if postData['desc'] < 5:
            errors['desc'] = "The description should be at least 5 characters!"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()