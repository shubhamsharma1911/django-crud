from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    name  = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    address = models.TextField()
    date = models.DateField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Team(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    lead = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

