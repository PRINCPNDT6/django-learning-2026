from django.db import models

# Create your models here.
class studentCards(models.Model):
    Name = models.CharField(max_length=100)
    RollNO = models.IntegerField()
    Email = models.EmailField(max_length=254)
    DateOfBirth = models.IntegerField()
    Course = models.CharField(max_length=50)
    About = models.TextField()
    image = models.ImageField(upload_to='cardsImg/')
    def __str__(self):
        return self.Name
