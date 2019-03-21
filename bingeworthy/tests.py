from django.test import TestCase
from bingeworthy.models import *
from django.core.urlresolvers import reverse

# Create your tests here.

class ShowMethodTests(TestCase):
    def test_show_slug_creation(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        self.assertEqual(show.slug, 'only-fools-and-horses')

    def test_create_show(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        self.assertTrue(isinstance(show,Show))       

    def test_at_init_no_views(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        self.assertEqual((show.views_total==0), True)

    def test_at_init_no_likes(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        self.assertEqual((show.like_ratio==0), True)

    def test_at_init_no_stars(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        self.assertEqual((show.star_rating==0), True)
    
    def test_calc_likes(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        viewer = Viewership(viewer=user, show=show, judgement=True)
        viewer.save()
        self.assertEqual((show.like_ratio==100),True)

    def test_calc_views(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        viewer = Viewership(viewer=user, show=show, judgement=True)
        viewer.save()
        self.assertEqual((show.views_total==1),True)

    def test_calc_stars(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        review = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review.save()
        self.assertEqual((show.star_rating==8),True)

class ReviewModelTests(TestCase):
    def test_create_review(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        review = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review.save()
        self.assertTrue(isinstance(review,Review))
    def test_auto_increment_id(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        review = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review2 = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review.save()
        review2.save()
        self.assertTrue(review.auto_increment_id != review2.auto_increment_id)

    def test_no_upvotes_at_init(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        review = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review.save()
        self.assertEqual(review.upvote_count==0,True)

    def test_upvote_counter(self):
        show = Show(title="Only Fools and Horses", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="aj", password="testaccount")
        user.save()
        review = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review.save()
        voteonreview = VotesOnReview(review=review, voter=user, judgement=True)
        voteonreview.save()
        self.assertEqual(review.upvote_count==1,True)
    
    