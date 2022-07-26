from django.db import models

'''This model is just for creating a book'''


class Book(models.Model):
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


'''Here This model contain the foreign key of book as well as it own.
Once a book is created we can then start adding sections of books. we
cannot add parent section and book in same section as I made hirechy 
so one child belongs to its parent only and so on and then end on
start of book.'''


class Section(models.Model):
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="sections", null=True, blank=True)
    parent_section = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name="child_sections", null=True, blank=True)
