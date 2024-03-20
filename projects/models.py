from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile,blank=True, null=True,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField( null=True , blank=True)
    featured_image = models.ImageField(default='icon.svg',blank=True, null=True)
    demo_link = models.CharField(max_length=2000 , blank=True , null=True)
    source_link = models.CharField(max_length=2000 , blank=True , null=True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default = 0 , blank=True, null=True)
    vote_ratio = models.FloatField(default = 0.0 , blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key = True , editable = False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
         ordering = ['-vote_ratio', '-vote_total', 'title']
    
    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
        
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='Up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()
        

class Review(models.Model):
    VOTE_TYPE = (('Up','Up Vote'),('Down','Down Vote'))
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length = 200, choices = VOTE_TYPE)
    
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key = True , editable = False)
    
    def __str__(self) -> str:
        return self.value
    # to keep limit that only one person can leave one unique comment per project.
    class Meta:
        unique_together = [['owner','project']]
        

class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key = True , editable = False)
    
    def __str__(self) -> str:
        return self.name