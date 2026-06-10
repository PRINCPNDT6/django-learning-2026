from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    Course = models.CharField(max_length=100, default='Python')


    def __str__(self):
        return self.name
    
#One to Many Relationship
class Review(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        ordering = ['-id']   # newest first
     

    # def __str__(self):
    #     return str(self.rating)