import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bingeworthy_project.settings')

import django
django.setup()
from bingeworthy.models import *

def populate():

######################show list begins here################################

	theOffice = {"title": "The Office (US)",
		"genre":"Comedy", "blurb": "A faux docuseries on the lives of workers at a paper company", 
		"starring": "Steve Carell", "platform": "Amazon Prime", "ep_runtime": 20, "num_episodes": 201, 
		"num_season": 9, "year_released": 2005}
	
	shows = [theOffice]
	
	for show in shows:
		show_added = add_show(show["title"], show["genre"], show["blurb"], show["starring"],
			show["platform"], show["ep_runtime"], show["num_episodes"], show["num_season"],
			show["year_released"])
	
#######################user list begins here#################################

	ajpod_test = {"username": "ajpod", "password":"ajpodtest"}
	gemma_test = {"username": "gemma", "password":"gemmatest"}
	
	users = [ajpod_test, gemma_test]
	print(users)
	
	for user in users:
		user_added = add_user(user["username"], user["password"])
	
####################review list begins here####################################
	print(User.objects.all())
	office_good = {"reviewer": User.objects.get(username = "ajpod"), "title": "It's good", "show": Show.objects.get(title = "The Office (US)"), "star_rating": 8,
	"review_body": "I thought this show was great, best ive watched in a long time"}
	
	reviews = [office_good]
	
	for review in reviews:
		review_added = add_review(review["reviewer"], review["title"], review["show"], review["star_rating"], review["review_body"])

######################viewership begins here####################################

	gemma_office = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "The Office (US)"), "judgement": True}
	
	viewerships = [gemma_office]
	
	for viewer in viewerships:
		viewer_added = add_viewership(viewer["viewer"], viewer["show"], viewer["judgement"])
		
######################votes on review#######################################

	gem_office_votes = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "gemma"), "judgement": True}
	
	votes = [gem_office_votes]
	
	for vote in votes:
		vote_added = add_vote(vote["review"], vote["voter"], vote["judgement"])
		

	
def add_show(title, genre, blurb, starring, platform, ep_runtime, num_episodes, 
num_season, year_released):
	show = Show.objects.get_or_create(title = title, genre = genre, blurb = blurb,
		starring = starring, platform = platform, ep_runtime = ep_runtime, num_episodes = num_episodes,
		num_season = num_season, year_released = year_released)[0]
	show.save()
	return show
	
def add_user(username, password):
	u = User.objects.get_or_create(username=username)[0]
	print(u)
	u.password = password
	u.save()
	return u
	
def add_review(reviewer, title, show, star_rating, review_body):
	review = Review.objects.get_or_create(reviewer = reviewer, title = title,
	show = show, star_rating = star_rating, review_body = review_body)[0]
	review.save()
	return review
	
def add_viewership(viewer, show, judgement):
	view = Viewership.objects.get_or_create(viewer = viewer, show = show, judgement = judgement)[0]
	view.save()
	return view
	
def add_vote(review, voter, judgement):
	vote = VotesOnReview.objects.get_or_create(review = review, voter = voter, judgement = judgement)[0]
	vote.save()
	return vote
	
	
		
if __name__ == '__main__':
	print("Starting Bingeworthy population script...")
	populate()
