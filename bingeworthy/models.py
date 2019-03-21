from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# TODO
# Add slugs if deemed necessary for URLs (probs necessary, not sure how to implement yet)
# Test it actually works
# Maybe add Meta subclasses like in Rango

class UserPicture(models.Model):  ## decided to just use main User model for everything
    user = models.OneToOneField(User, primary_key = True)

    picture = models.ImageField(upload_to='profile_images', blank=True)

class Genre(models.Model):
    genre = models.CharField(max_length=30)

class Platform(models.Model):
    platform = models.CharField(max_length=30)

		

class Show(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    blurb = models.CharField(max_length=200)
    starring = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='show_images', blank=True)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)

    @property
    def star_rating(self):
        stars=0
        for r in Review.objects.filter(show__exact=self):
            stars+= r.star_rating
        if Review.objects.filter(show__exact=self).count() > 0:		
            return round(stars/Review.objects.filter(show__exact=self).count(), 1)
        else:
            return 0

    @property
    def like_ratio(self):
        likes=0
        for v in Viewership.objects.filter(show__exact=self):
            if v.judgement:
                likes+=1
        if Viewership.objects.filter(show__exact=self).count() > 0:
            return round(likes/Viewership.objects.filter(show__exact=self).count(), 2)*100
        else:
            return 0

    @property
    def views_total(self):
        return Viewership.objects.filter(show__exact=self).count()

    ep_runtime = models.IntegerField(validators=[MinValueValidator(0)])
    num_episodes = models.IntegerField(validators=[MinValueValidator(1)])
    num_season = models.IntegerField(validators=[MinValueValidator(1)])
    year_released = models.IntegerField()
    
    viewers = models.ManyToManyField(User, through='Viewership') # M-N field with judgement variable

    def __str__(self):
        return self.title 
		
    def save(self, *args, **kwargs):
	    self.slug = slugify(self.title)
	    super(Show, self).save(*args, **kwargs)

class Viewership(models.Model):
    # the whole idea of this and especially models.CASCADE part is from the django docs
    viewer = models.ForeignKey(User, on_delete = models.CASCADE)
    show = models.ForeignKey(Show, on_delete = models.CASCADE)
    judgement = models.BooleanField()

class Review(models.Model):
    # got this from stackoverflow, apparently Django can't do compound primary keys
    # when they're both foreign keys from elsewhere
    auto_increment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    # note the use of related_name attribute
    # this is because reviewer and votes both refer to the same field, 
    # namely using UserAccount as foreign key.
    # using related_name solves the conflict which stopped the migration working
    reviewer = models.ForeignKey(User, related_name='reviewer_user', on_delete=models.CASCADE)
    star_rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    review_body = models.CharField(max_length=1000)
    
    votes = models.ManyToManyField(User, through='VotesOnReview', related_name='voter_user')

    # call Review.upvote_count to get, like a normal field, sort of
    # taken from a reddit thread https://www.reddit.com/r/django/comments/8tyv4n/calculated_model_fields/
    @property
    def upvote_count(self):
        # doesn't work if you declare up and down on same line
        up = 0
        down = 0
        # don't question the following code, took me forever and a lot of 
        # python shell pain to get it so let's just pray it works
        for v in self.votes.all():
            if VotesOnReview.objects.get(voter__exact=v, review__exact=self).judgement == True:
                up+=1
            else:
                down+=1
        return up-down
    


    def __str__(self):
        return str(self.title)


class VotesOnReview(models.Model):
    voter = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    judgement = models.BooleanField()

