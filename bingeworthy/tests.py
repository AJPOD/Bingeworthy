from django.test import TestCase, Client
from bingeworthy.models import *
from bingeworthy.forms import *
from django.core.urlresolvers import reverse

# Create your tests here.

class ShowModelTests(TestCase):
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

class IndexViewTests(TestCase):
    def test_index_view_loads(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Featured Show")

class LoginViewTests(TestCase):
    def test_login_redirects_if_user_authenticated(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="ajpod")
        user.set_password("testaccount")
        user.save()
        self.client.login(username="ajpod", password="testaccount")
        response = self.client.get(reverse('login'), follow=True)
        self.assertContains(response, "Featured Show")
    
    def test_signup_form_is_valid(self):
        self.user = {'email': "solskjaer@gmail.com", 'username': 'ajpod', 'password':'testpassword'}
        form = UserForm(self.user)
        self.assertTrue(form.is_valid())   

class LogoutViewTests(TestCase):
    def test_logout_redirects_if_not_logged_in(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        response = self.client.get(reverse('logout'), follow=True)
        self.assertContains(response, "Featured Show")   

    def test_logout_logs_out(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="ajpod")
        user.set_password("testaccount")
        user.save()
        self.client.login(username="ajpod", password="testaccount")
        response = self.client.get(reverse('logout'), follow=True)
        self.assertContains(response, "Featured Show")         
        self.assertNotIn('_auth_user_id', self.client.session)

class ShowShowViewTests(TestCase):
    def test_shows_show(self):
        show1 = Show(title="The Office (US)", blurb= "s", starring= "Michael Gary Scott", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show1.save()
        show2 = Show(title="ofah", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show2.save()
        show3 = Show(title="father ted", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show3.save()
        show4 = Show(title="fawlty", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show4.save()              
        response = self.client.get(reverse('shows_show', kwargs={'show_name_slug': show1.slug}))
        self.assertContains(response, "Starring: Michael Gary Scott")
        self.assertContains(response, "fawlty")
        self.assertContains(response, "father-ted")
        self.assertContains(response, "ofah")
    
class MakeReviewViewTests(TestCase):
    def test_review_redirects_if_user_not_authenticated(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "Michael Gary Scott", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        response = self.client.get(reverse('make_review', kwargs={'show_name_slug': show.slug}), follow=True)
        self.assertContains(response, "Register")

    def test_review_form_hidden_when_not_viewed(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="ajpod")
        user.set_password("testaccount")
        user.save()
        self.client.login(username="ajpod", password="testaccount")  
        response = self.client.get(reverse('make_review', kwargs={'show_name_slug': show.slug}), follow=True)
        self.assertContains(response, "You have not watched this show.")
        self.assertNotContains(response, "Review Body")

    def test_review_form_hidden_when_already_reviewed(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="ajpod")
        user.set_password("testaccount")
        user.save()
        self.client.login(username="ajpod", password="testaccount")  
        viewer = Viewership(viewer=user, show=show, judgement=True)
        viewer.save()
        review = Review(reviewer=user, show=show, title="hello", review_body="hello", star_rating=8)
        review.save()
        response = self.client.get(reverse('make_review', kwargs={'show_name_slug': show.slug}), follow=True)
        self.assertContains(response, "You have already made a review.")
        self.assertNotContains(response, "Review Body")

    def test_review_form_shows_otherwise(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="ajpod")
        user.set_password("testaccount")
        user.save()
        self.client.login(username="ajpod", password="testaccount")  
        viewer = Viewership(viewer=user, show=show, judgement=True)
        viewer.save()
        response = self.client.get(reverse('make_review', kwargs={'show_name_slug': show.slug}), follow=True)
        self.assertContains(response, "Review Body")
        self.assertNotContains(response, "You have already made a review.")
        self.assertNotContains(response, "You have not watched this show.")       

    def test_review_form_is_valid(self):
        show = Show(title="The Office (US)", blurb= "s", starring= "g", ep_runtime=40, num_episodes=100, num_season=7, year_released=1980)
        show.save()
        user = User(username="ajpod")
        user.set_password("testaccount")
        review = {'title': 'hello', 'review_body': 'ding dong', 'star_rating': 8 }
        form = ReviewForm(review)
        self.assertTrue(form.is_valid())  



    



