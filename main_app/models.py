from django.db import models

class FriendsModel(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    contact_no = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


    