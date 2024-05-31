from django.db import models
import uuid 
from users.models import Profile

# Create your models here.
class Painting(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
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

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    def getVoteScore(self):
        reviews = self.review_set.all()
        total_score = 0
        
        for review in reviews:
            total_score += int(review.value)
        self.vote_total = reviews.count()
        self.vote_score = int(round(total_score / self.vote_total))
        self.save()


    class Meta:
        ordering = ['-vote_score', "-vote_total", "title"]
    
class Review(models.Model):
    VOTE_TYPE = [("1", "Just Pass👌🏼"), 
                ("2", "Nice👍"), 
                ("3", 'Look Good!😍'),
                ("4", 'Wonderful!🤩')]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    
    class Meta:
        unique_together = [['owner', 'painting']]
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

