import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bingeworthy_project.settings')

import django
django.setup()
from bingeworthy.models import *

def populate():

	genres = ["Comedy", "Sci-Fi", "Horror", "Romance", "Action", "Thriller", "Drama", "Crime", "Animation", "Fantasy", "Reality"]
	platforms = ["Amazon Prime", "Netflix", "Hayu", "BBC iPlayer"]
	
	for genre in genres:
		genre_added = add_genre(genre)
		
	for platform in platforms:
		platform_added = add_platform(platform)

######################show list begins here################################

	theOffice = {"title": "The Office (US)", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "A faux docuseries depicting the lives of office workers at a paper company.", 
		"starring": "Steve Carell", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 20, "num_episodes": 201, "num_season": 9, "year_released": 2005}
		
	greysAnatomy = {"title": "Grey's Anatomy", "genre":Genre.objects.get(genre = "Drama"), 
		"blurb": "Grey's Anatomy is an American medical drama show. The fictional show focuses on the lives of surgical interns, residents and attending physicians as the try to maintain personal lives as they work.", 
		"starring": "Ellen Pompeo", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 20, "num_episodes": 334, "num_season": 15, "year_released": 2005}
		
	friends = {"title": "Friends", "genre":Genre.objects.get(genre = "Comedy"), 
		"blurb": "A sitcom following six friends living and working in New York.", 
		"starring": "Jennifer Annistion", "platform": Platform.objects.get(platform = "Netflix"), "ep_runtime": 20, "num_episodes": 236, 
		"num_season": 10, "year_released": 1994}
		
	supernatural = {"title": "Supernatural", "genre":Genre.objects.get(genre = "Fantasy"), 
		"blurb": "A dark fantasy show about two brothers who fight evil supernatural beings that roam the earth.", 
		"starring": "Jenson Ackles", "platform": Platform.objects.get(platform = "Amazon Prime"), "ep_runtime": 40, "num_episodes": 300, 
		"num_season": 14, "year_released": 2005}
		
	theVampireDiaries = {"title": "The Vampire Diaries", "genre":Genre.objects.get(genre = "Fantasy"), 
		"blurb": "Trapped in adolescent bodies, feuding vampire brothers Stefan and Damon fight for the affection of captivating teenager Elena.", 
		"starring": "Nina Dobrev", "platform": Platform.objects.get(platform = "Netflix"), "ep_runtime": 40, "num_episodes": 171, 
		"num_season": 8, "year_released": 2009}
		
	mockTheWeek = {"title": "Mock the Week", "genre":Genre.objects.get(genre = "Comedy"), 
		"blurb": "A British, satirical celebrity panel show, where comedians discuss the news events from the week.", 
		"starring": "Dara O'Briain", "platform": Platform.objects.get(platform = "BBC iPlayer"), "ep_runtime": 30, "num_episodes": 188, 
		"num_season": 17, "year_released": 2005}

	brooklynNineNine = {"title": "Brooklyn Nine Nine", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "Follow the happy-go-lucky detective, Jake Peralta, in his shenanigans in New York with his precinct.", 
		"starring": "Andy Samberg", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 20, "num_episodes": 122, "num_season": 6, "year_released": 2013}
		
	
	
	shows = [theOffice, greysAnatomy, friends, supernatural, theVampireDiaries, mockTheWeek, brooklynNineNine]
	
	for show in shows:
		show_added = add_show(show["title"], show["genre"], show["blurb"], show["starring"],
			show["platform"], show["ep_runtime"], show["num_episodes"], show["num_season"],
			show["year_released"])
	
#######################user list begins here#################################

	ajpodUser = {"username": "ajpod", "password":"ajpodtest"}
	gemmaUser = {"username": "gemma", "password":"gemmatest"}
	zeerakUser = {"username": "zeerak", "password": "zeeraktest"}
	thomasUser = {"username": "thomas", "password": "thomastest"}
	
	users = [ajpodUser, gemmaUser, zeerakUser, thomasUser]
	
	for user in users:
		user_added = add_user(user["username"], user["password"])
	
####################review list begins here####################################
	
	office_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "It's good", 
	"show": Show.objects.get(title = "The Office (US)"), "star_rating": 8,
	"review_body": "I thought this show was great, best ive watched in a long time"}
	
	office_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "New fave show", 
	"show": Show.objects.get(title = "The Office (US)"), "star_rating": 10,
	"review_body": "This is my new favourite show, I'm going to be quoting this for years!!"}
	
	greys_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "So tense", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 7,
	"review_body": "I really liked this, you get very emotionally attatched to the characters"}
	
	greys_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Graphic", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 1,
	"review_body": "You definitely cant be squeamish for this, its super gorey!"}
	
	friends_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Oldy but goody", 
	"show": Show.objects.get(title = "Friends"), "star_rating": 9,
	"review_body": "Its a classic show, always good to throw on in the background while you do something."}
	
	friends_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Pretty good", 
	"show": Show.objects.get(title = "Friends"), "star_rating": 8,
	"review_body": "Always liked this show, its a good one to rewatch"}
	
	supernatural_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "So good", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 10,
	"review_body": "I loved this show, its action filled and scary too"}
	
	supernatural_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Scary", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 5,
	"review_body": "Think this is a bit too dark for me, the characters were likable though"}
	
	vampDiaries_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Too angsty", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 3,
	"review_body": "The dialogue in this is pretty bad and the storyline is predictable"}
	
	vampDiaries_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Twilight-y", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 0,
	"review_body": "Its made for teens, if you enjoyed Twilight then youd like this."}
	
	mtw_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Best panel show", 
	"show": Show.objects.get(title = "Mock the Week"), "star_rating": 9,
	"review_body": "Really good panel show, its more about the jokes than the news though"}
	
	mtw_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Watch it every week", 
	"show": Show.objects.get(title = "Mock the Week"), "star_rating": 10,
	"review_body": "Its the only panel show i watch, i love it"}
	
	
	reviews = [office_review1, office_review2, greys_review1, greys_review2, friends_review1, 
	friends_review2, supernatural_review1, supernatural_review2, vampDiaries_review1, vampDiaries_review2,
	mtw_review1, mtw_review2 ]
	
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
		

	
def add_genre(genre):
	genre = Genre.objects.get_or_create(genre = genre)[0]
	genre.save()
	return genre

def add_platform(platform):
	platform = Platform.objects.get_or_create(platform = platform)[0]
	platform.save()
	return platform
	
def add_show(title, genre, blurb, starring, platform, ep_runtime, num_episodes, 
num_season, year_released):
	show = Show.objects.get_or_create(title = title, genre = genre, blurb = blurb,
		starring = starring, platform = platform, ep_runtime = ep_runtime, num_episodes = num_episodes,
		num_season = num_season, year_released = year_released)[0]
	show.save()
	return show
	
def add_user(username, password):
	u = User.objects.get_or_create(username=username)[0]
	#print(u)
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
