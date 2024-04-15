from django.db import models
from django.contrib.auth.models import User

# Choices for block_name field
CHOOSE_ONE = (
    ("smvb", "Sir M Visvesvarya Block (SMVB)"),
    ("cvr", "CV Raman Block"),
)

class Item(models.Model):
    block_name = models.CharField(choices=CHOOSE_ONE, max_length=50)
    room_number_or_name_of_audi = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='room_images/')  # Define ImageField

    def __str__(self):
        return self.room_number_or_name_of_audi
