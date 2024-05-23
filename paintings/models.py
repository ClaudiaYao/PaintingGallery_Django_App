from django.db import models
import uuid 

# Create your models here.
class Painting(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    demo_link = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_score = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = [("Average", 1), 
                 ("Nice", 2), 
                 ('Great', 3),
                 ('Amazing', 4)]
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

