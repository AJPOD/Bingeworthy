from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

# TODO
# Add slugs if deemed necessary for URLs (probs necessary, not sure how to implement yet)
# Test it actually works
# Maybe add Meta subclasses like in Rango

class UserAccount(models.Model):  ## called user because User is already a default thing imported above
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Show(models.Model):
    title = models.CharField(max_length=60)
    genre = models.CharField(max_length=30)
    star_rating = models.FloatField()
    like_ration = models.IntegerField()
    blurb = models.CharField(max_length=200)
    starring = models.CharField(max_length=100)
    picture = models.ImageField()
    platform = models.CharField(max_length=30)
    views_total = models.IntegerField()
    ep_runtime = models.IntegerField()
    num_episodes = models.IntegerField()
    num_season = models.IntegerField()
    year_released = models.IntegerField()
    
    viewers = models.ManyToManyField(UserAccount, through='Viewership') # M-N field with judgement variable

    def __str__(self):
        return self.title 

class Viewership(models.Model):
    # the whole idea of this and especially models.CASCADE part is from the django docs
    viewer = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    judgement = models.BooleanField()

class Review(models.Model):
    # got this from stackoverflow, apparently Django can't do compound primary keys
    # when they're both foreign keys from elsewhere
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    show = models.ForeignKey(Show)

    # note the use of related_name attribute
    # this is because reviewer and votes both refer to the same field, 
    # namely using UserAccount as foreign key.
    # using related_name solves the conflict which stopped the migration working
    reviewer = models.ForeignKey(UserAccount, related_name='reviewer_user')
    star_rating = models.IntegerField()
    review_body = models.CharField(max_length=1000)
    
    votes = models.ManyToManyField(UserAccount, through='VotesOnReview', related_name='voter_user')

    # call Review.upvote_count to get, like a normal field, sort of
    # taken from a reddit thread https://www.reddit.com/r/django/comments/8tyv4n/calculated_model_fields/
    @property
    def upvote_count(self):
        # doesn't work if you declare up and down on same line
        up = 0
        down = 0
        for v in self.votes.all():
            if VotesOnReview.objects.get(voter__exact=v, review__exact=self).judgement == True:
                up+=1
            else:
                down+=1
        return up-down


    def __str__(self):
        return self.title

class VotesOnReview(models.Model):
    voter = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    judgement = models.BooleanField()
