import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bingeworthy_project.settings')

import django
django.setup()
from bingeworthy.models import *

def populate():

	genres = ["Comedy", "Sci-Fi", "Fantasy", "Thriller", "Drama", "Crime", "Reality"]
	platforms = ["Amazon Prime", "Netflix", "Hayu", "BBC iPlayer", "Sky Go"]
	
	for genre in genres:
		genre_added = add_genre(genre)
		
	for platform in platforms:
		platform_added = add_platform(platform)

######################show list begins here################################
	#COMEDY
	theOffice = {"title": "The Office (US)", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "A faux docuseries depicting the lives of office workers at a paper company.", 
		"starring": "Steve Carell", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 20, "num_episodes": 201, "num_season": 9, "year_released": 2005}
		
	friends = {"title": "Friends", "genre":Genre.objects.get(genre = "Comedy"), 
		"blurb": "A sitcom following six friends living and working in New York.", 
		"starring": "Jennifer Annistion", "platform": Platform.objects.get(platform = "Netflix"), "ep_runtime": 20, "num_episodes": 236, 
		"num_season": 10, "year_released": 1994}
		
	brooklynNineNine = {"title": "Brooklyn Nine Nine", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "Follow the happy-go-lucky detective, Jake Peralta, in his shenanigans in New York with his precinct.", 
		"starring": "Andy Samberg", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 20, "num_episodes": 122, "num_season": 6, "year_released": 2013}
		
	community = {"title": "Community", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "A group of misfits become friends as the study at Greendale Community College", 
		"starring": "Joel McHale", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 20, "num_episodes": 110, "num_season": 6, "year_released": 2015}
		
	mockTheWeek = {"title": "Mock the Week", "genre":Genre.objects.get(genre = "Comedy"), 
		"blurb": "A British, satirical celebrity panel show, where comedians discuss the news events from the week.", 
		"starring": "Dara O'Briain", "platform": Platform.objects.get(platform = "BBC iPlayer"), "ep_runtime": 30, "num_episodes": 188, 
		"num_season": 17, "year_released": 2005}
		
	#SCI-FI
	strangerThings = {"title": "Stranger Things", "genre": Genre.objects.get(genre = "Sci-Fi"), 
		"blurb": "When a young boy goes missing, a mystery involving secret experiments and the supernatural is uncovered.", 
		"starring": "Winona Ryder", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 50, "num_episodes": 17, "num_season": 2, "year_released": 2016}
		
	doctorWho = {"title": "Doctor Who", "genre": Genre.objects.get(genre = "Sci-Fi"), 
		"blurb": "A show depicting the adventures of a Time Lord called 'The Docter' and his companion", 
		"starring": "David Tennant", "platform": Platform.objects.get(platform = "BBC iPlayer"), 
		"ep_runtime": 45, "num_episodes": 851, "num_season": 37, "year_released": 1963}
		
	blackMirror = {"title": "Black Mirror", "genre": Genre.objects.get(genre = "Sci-Fi"), 
		"blurb": "Anthology that examines modern society and consequences of new technology.", 
		"starring": "Will Poulter", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 40, "num_episodes": 19, "num_season": 4, "year_released": 2011}
		
	starTrek = {"title": "Star Trek", "genre":Genre.objects.get(genre = "Sci-Fi"), 
		"blurb": "This follows the interstellar adventures of Capt Kirk and his crew.", 
		"starring": "William Shatner", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 50, "num_episodes": 79, "num_season": 3, "year_released": 1966}
		
	#FANTASY
	supernatural = {"title": "Supernatural", "genre":Genre.objects.get(genre = "Fantasy"), 
		"blurb": "A dark fantasy show about two brothers who fight evil supernatural beings that roam the earth.", 
		"starring": "Jenson Ackles", "platform": Platform.objects.get(platform = "Amazon Prime"), "ep_runtime": 40, "num_episodes": 300, 
		"num_season": 14, "year_released": 2005}
		
	theVampireDiaries = {"title": "The Vampire Diaries", "genre":Genre.objects.get(genre = "Fantasy"), 
		"blurb": "Trapped in adolescent bodies, feuding vampire brothers Stefan and Damon fight for the affection of captivating teenager Elena.", 
		"starring": "Nina Dobrev", "platform": Platform.objects.get(platform = "Netflix"), "ep_runtime": 40, "num_episodes": 171, 
		"num_season": 8, "year_released": 2009}
	
	gameOfThrones = {"title": "Game of Thrones", "genre": Genre.objects.get(genre = "Fantasy"), 
		"blurb": "Young family adopts litter of dogs, hilarity ensues", 
		"starring": "Sean Bean", "platform": Platform.objects.get(platform = "Sky Go"), 
		"ep_runtime": 50, "num_episodes": 67, "num_season": 7, "year_released": 2011}
		
	lotr = {"title": "Lord of the Rings", "genre": Genre.objects.get(genre = "Fantasy"), 
		"blurb": "Second age shenanigans", 
		"starring": "JRR Tolkien", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 30, "num_episodes": 1, "num_season": 1, "year_released": 2020}
		
	#THRILLER
	theWalkingDead = {"title": "The Walking Dead", "genre": Genre.objects.get(genre = "Thriller"), 
		"blurb": "Survivors of the apocalypse try to stay alive under the constant threat of mindless zombies", 
		"starring": "Andrew Lincoln", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 50, "num_episodes": 129, "num_season": 9, "year_released": 2010}
	
	mrRobot = {"title": "Mr Robot", "genre": Genre.objects.get(genre = "Thriller"), 
		"blurb": "A cybersecurity engineer gets recruited by an anarchist called Mr Robot", 
		"starring": "Rami Malek", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 50, "num_episodes": 32, "num_season": 3, "year_released": 2015}
	
	luther = {"title": "Luther", "genre": Genre.objects.get(genre = "Thriller"), 
		"blurb": "Luther is a detective who ruthlessly chases criminals while at times getting consumed by the darkness of these crimes", 
		"starring": "Idris Elba", "platform": Platform.objects.get(platform = "BBC iPlayer"), 
		"ep_runtime": 60, "num_episodes": 20, "num_season": 5, "year_released": 2010}
		
	you = {"title": "You", "genre": Genre.objects.get(genre = "Thriller"), 
		"blurb": "A bookseller who falls in love with a customer and quickly becomes obsessed with her", 
		"starring": "Penn Badgley", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 45, "num_episodes": 10, "num_season": 1, "year_released": 2018}
		
	#DRAMA
	bigLittleLies = {"title": "Big Little Lies", "genre": Genre.objects.get(genre = "Drama"), 
		"blurb": "A series that tells the tale of three mothers whose seemingly perfect lives crumble to the point of murder", 
		"starring": "Reese Witherspoon", "platform": Platform.objects.get(platform = "Sky Go"), 
		"ep_runtime": 50, "num_episodes": 7, "num_season": 1, "year_released": 2017}
		
	greysAnatomy = {"title": "Grey's Anatomy", "genre":Genre.objects.get(genre = "Drama"), 
		"blurb": "Grey's Anatomy is an American medical drama show. The fictional show focuses on the lives of surgical interns, residents and attending physicians as the try to maintain personal lives as they work.", 
		"starring": "Ellen Pompeo", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 20, "num_episodes": 334, "num_season": 15, "year_released": 2005}
		
	theHandMaidsTale = {"title": "The Handmaids Tale", "genre": Genre.objects.get(genre = "Drama"), 
		"blurb": "A dystopian future where fertile women are forced to become child-bearing slaves called 'handmaids'", 
		"starring": "Elizabeth Moss", "platform": Platform.objects.get(platform = "Sky Go"), 
		"ep_runtime": 50, "num_episodes": 23, "num_season": 2, "year_released": 2017}
	
	peakyBlinders = {"title": "Peaky Blinders", "genre": Genre.objects.get(genre = "Drama"), 
		"blurb": "Follows the exploits of Shelby crime family after World War I", 
		"starring": "Cillian Murphy", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 55, "num_episodes": 24, "num_season": 4, "year_released": 2013}
	
	#CRIME
	dahmerOnDahmer = {"title": "Dahmer On Dahmer", "genre": Genre.objects.get(genre = "Crime"), 
		"blurb": "A look iinside the twisted mind of Jeffrey Dahmer, a notorious serial killer", 
		"starring": "Jeffrey Dahmer", "platform": Platform.objects.get(platform = "Hayu"), 
		"ep_runtime": 45, "num_episodes": 2, "num_season": 1, "year_released": 2017}
		
	htgawm = {"title": "How to Get Away with Murder", "genre": Genre.objects.get(genre = "Crime"), 
		"blurb": "A law professor and her students become entwined in a murder plot", 
		"starring": "Viola Davis", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 40, "num_episodes": 75, "num_season": 5, "year_released": 2014}
		
	iceColdBlood = {"title": "In Ice Cold Blood", "genre": Genre.objects.get(genre = "Crime"), 
		"blurb": "Ice-T exposes outrageous true crime stories", 
		"starring": "Ice T", "platform": Platform.objects.get(platform = "Hayu"), 
		"ep_runtime": 40, "num_episodes": 8, "num_season": 1, "year_released": 2018}
		
	shetland = {"title": "Shetland", "genre": Genre.objects.get(genre = "Crime"), 
		"blurb": "Detective helps Steland police solve a mysterious murder.", 
		"starring": "Douglas Henshall", "platform": Platform.objects.get(platform = "BBC iPlayer"), 
		"ep_runtime": 60, "num_episodes": 26, "num_season": 5, "year_released": 2013}
		
	#REALITY
	kuwtk = {"title": "Keeping Up with the Kardashians", "genre": Genre.objects.get(genre = "Reality"), 
		"blurb": "The show focuses on personal and professional lives of the Kardashian-Jenner blended family", 
		"starring": "Kim Kardashian", "platform": Platform.objects.get(platform = "Hayu"), 
		"ep_runtime": 40, "num_episodes": 230, "num_season": 15, "year_released": 2007}
	
	millionaireMatchmaker = {"title": "Millionaire Matchmaker", "genre": Genre.objects.get(genre = "Reality"), 
		"blurb": "Millionaires try to find love from a group of selected women", 
		"starring": "Patti Stranger", "platform": Platform.objects.get(platform = "Hayu"), 
		"ep_runtime": 40, "num_episodes": 106, "num_season": 8, "year_released": 2008}

	theApprectice = {"title": "The Apprentice", "genre": Genre.objects.get(genre = "Reality"), 
		"blurb": "A business styled reality game show", 
		"starring": "Alan Sugar", "platform": Platform.objects.get(platform = "BBC iPlayer"), 
		"ep_runtime": 60, "num_episodes": 196, "num_season": 14, "year_released": 2005}
	
	catfish = {"title": "Catfish", "genre": Genre.objects.get(genre = "Reality"), 
		"blurb": "Nev shows the truths and lies about online dating", 
		"starring": "Nev Schulman", "platform": Platform.objects.get(platform = "Sky Go"), 
		"ep_runtime": 40, "num_episodes": 116, "num_season": 7, "year_released": 2012}
	
	shows = [theOffice, friends, brooklynNineNine, community, mockTheWeek, 
	strangerThings, doctorWho, blackMirror, starTrek,
	supernatural, theVampireDiaries, gameOfThrones, lotr,
	theWalkingDead, mrRobot, luther, you,
	bigLittleLies, greysAnatomy, theHandMaidsTale, peakyBlinders,
	dahmerOnDahmer, htgawm, iceColdBlood, shetland,
	kuwtk, millionaireMatchmaker, theApprectice, catfish
	]
	
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
	"show": Show.objects.get(title = "The Office (US)"), "star_rating": 10,
	"review_body": "I thought this show was great, best ive watched in a long time"}
	
	office_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "New fave show", 
	"show": Show.objects.get(title = "The Office (US)"), "star_rating": 10,
	"review_body": "This is my new favourite show, I'm going to be quoting this for years!!"}
	
	office_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "I liked it", 
	"show": Show.objects.get(title = "The Office (US)"), "star_rating": 9,
	"review_body": "It takes a while to get into it but it was better than i thought"}
	
	office_review4 = {"reviewer": User.objects.get(username = "gemma"), "title": "Super funny", 
	"show": Show.objects.get(title = "The Office (US)"), "star_rating": 10,
	"review_body": "I really liked this show, definitely bingeworthy. I could watch this for days."}
	
	friends_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Oldy but goody", 
	"show": Show.objects.get(title = "Friends"), "star_rating": 9,
	"review_body": "Its a classic show, always good to throw on in the background while you do something."}
	
	friends_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Pretty good", 
	"show": Show.objects.get(title = "Friends"), "star_rating": 8,
	"review_body": "Always liked this show, its a good one to rewatch"}
	
	friends_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Wasnt for me", 
	"show": Show.objects.get(title = "Friends"), "star_rating": 4,
	"review_body": "Can see why people would like it but it wasnt really my thing"}
	
	mtw_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Best panel show", 
	"show": Show.objects.get(title = "Mock the Week"), "star_rating": 9,
	"review_body": "Really good panel show, its more about the jokes than the news though"}
	
	mtw_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Watch it every week", 
	"show": Show.objects.get(title = "Mock the Week"), "star_rating": 10,
	"review_body": "Its the only panel show i watch, i love it"}
	
	mtw_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Already like it", 
	"show": Show.objects.get(title = "Mock the Week"), "star_rating": 8,
	"review_body": "Just started watching it and its really funny"}
	
	b99_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Great characters", 
	"show": Show.objects.get(title = "Brooklyn Nine Nine"), "star_rating": 8,
	"review_body": "Characters are really funny"}
	
	b99_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Doesnt dry up", 
	"show": Show.objects.get(title = "Brooklyn Nine Nine"), "star_rating": 7,
	"review_body": "With shows like this they can dry up but this stays funny"}
	
	b99_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Dont like it", 
	"show": Show.objects.get(title = "Brooklyn Nine Nine"), "star_rating": 2,
	"review_body": "I didnt find it very funny to be honest"}
	
	community_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Its alright", 
	"show": Show.objects.get(title = "Community"), "star_rating": 5,
	"review_body": "Its not the best, not the worst"}
	
	community_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Love it", 
	"show": Show.objects.get(title = "Community"), "star_rating": 10,
	"review_body": "This show is great, exactly what ive been looking for"}
	
	community_review3 = {"reviewer": User.objects.get(username = "gemma"), "title": "Surprisingly good", 
	"show": Show.objects.get(title = "Community"), "star_rating": 7,
	"review_body": "Didnt think I'd like it but it was actually really funny"}

	strangerThings_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Great theme", 
	"show": Show.objects.get(title = "Stranger Things"), "star_rating": 7,
	"review_body": "Really good show but the theme is the best part"}
	
	strangerThings_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Scary enough", 
	"show": Show.objects.get(title = "Stranger Things"), "star_rating": 7,
	"review_body": "Its a good level of scary without being horror"}
	
	strangerThings_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "80s era", 
	"show": Show.objects.get(title = "Stranger Things"), "star_rating": 8,
	"review_body": "A really good 80s era show"}
	
	docWho_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "My favourite", 
	"show": Show.objects.get(title = "Doctor Who"), "star_rating": 10,
	"review_body": "All time favourite show"}
	
	docWho_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Hated it", 
	"show": Show.objects.get(title = "Doctor Who"), "star_rating": 1,
	"review_body": "Only good if youre into old shows"}
	
	docWho_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Very old", 
	"show": Show.objects.get(title = "Doctor Who"), "star_rating": 6,
	"review_body": "First time watching an old show but its not too bad"}
	
	blackMirror_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Eye opening", 
	"show": Show.objects.get(title = "Black Mirror"), "star_rating": 9,
	"review_body": "Really makes you think"}
	
	blackMirror_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Disturbing", 
	"show": Show.objects.get(title = "Black Mirror"), "star_rating": 6,
	"review_body": "Quite haunting, enjoyed it though"}
	
	blackMirror_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "So cool", 
	"show": Show.objects.get(title = "Black Mirror"), "star_rating": 9,
	"review_body": "Never seen a show like this"}
	
	starTrek_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Good for an old show", 
	"show": Show.objects.get(title = "Star Trek"), "star_rating": 7,
	"review_body": "Not as good as doctor who but I quite liked it"}
	
	starTrek_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "New one is better",
	"show": Show.objects.get(title = "Star Trek"), "star_rating": 6,
	"review_body": "Its okay but the newer version is better"}
	
	starTrek_review3 = {"reviewer": User.objects.get(username = "gemma"), "title": "Old school", 
	"show": Show.objects.get(title = "Star Trek"), "star_rating": 7,
	"review_body": "Its an old show but its still good to watch"}

	supernatural_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "So good", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 10,
	"review_body": "I loved this show, its action filled and scary too"}
	
	supernatural_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Scary", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 5,
	"review_body": "Think this is a bit too dark for me, the characters were likable though"}

	supernatural_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Its meh", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 6,
	"review_body": "Similar to other shows in the same style"}
	
	vampDiaries_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Too angsty", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 3,
	"review_body": "The dialogue in this is pretty bad and the storyline is predictable"}
	
	vampDiaries_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Twilight-y", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 1,
	"review_body": "Its made for teens, if you enjoyed Twilight then you would like this."}
	
	vampDiaries_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "This is bad", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 1,
	"review_body": "Really easy to get bored of it"}
	
	got_review1 = {"reviewer": User.objects.get(username = "thomas"), "title": "Best show ever", 
	"show": Show.objects.get(title = "Game of Thrones"), "star_rating": 10,
	"review_body": "This is one of the best shows ive ever seen"}
	
	got_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Middle seasons arent great", 
	"show": Show.objects.get(title = "Game of Thrones"), "star_rating": 8,
	"review_body": "The seasons in the middle arent great but its gets better recently"}
	
	got_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "This is everything", 
	"show": Show.objects.get(title = "Game of Thrones"), "star_rating": 10,
	"review_body": "This show has something for everyone, definetly bingeworthy, definitely rewatchable"}
	
	lotr_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Not out yet", 
	"show": Show.objects.get(title = "Lord of the Rings"), "star_rating": 9,
	"review_body": "Not out yet but i know its gonna be good"}
	
	lotr_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Excited to try it", 
	"show": Show.objects.get(title = "Lord of the Rings"), "star_rating": 8,
	"review_body": "Im not a diehard fan but im excited to see this"}
	
	lotr_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Hyped", 
	"show": Show.objects.get(title = "Lord of the Rings"), "star_rating": 9,
	"review_body": "So hyped for this to come out in 2020"}

	twd_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Good", 
	"show": Show.objects.get(title = "The Walking Dead"), "star_rating": 9,
	"review_body": "Really liked this"}
	
	twd_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Gorey", 
	"show": Show.objects.get(title = "The Walking Dead"), "star_rating": 9,
	"review_body": "Pretty gorey but still a really great show"}
	
	twd_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Stopped watching", 
	"show": Show.objects.get(title = "The Walking Dead"), "star_rating": 2,
	"review_body": "Sort of lost interest after a while"}
	
	mrRobot_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Lead actor was great", 
	"show": Show.objects.get(title = "Mr Robot"), "star_rating": 7,
	"review_body": "Really liked the starring actor"}
	
	mrRobot_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Acting was great", 
	"show": Show.objects.get(title = "Mr Robot"), "star_rating": 7,
	"review_body": "The acting was really great in this show"}
	
	mrRobot_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Rami malek", 
	"show": Show.objects.get(title = "Mr Robot"), "star_rating": 7,
	"review_body": "Rami malek totally makes this show, would love to see more with him in it"}
	
	luther_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Wouldnt recommend", 
	"show": Show.objects.get(title = "Luther"), "star_rating": 4,
	"review_body": "Similar to many crime shows"}
	
	luther_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Predictable", 
	"show": Show.objects.get(title = "Luther"), "star_rating": 4,
	"review_body": "You know whats going to happen in it and so that ruins any sense of tension"}
	
	luther_review3 = {"reviewer": User.objects.get(username = "gemma"), "title": "Didnt like it", 
	"show": Show.objects.get(title = "Luther"), "star_rating": 4,
	"review_body": "Its not very good to be honest, i dont think its very bingeworthy"}
	
	you_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Sooo good", 
	"show": Show.objects.get(title = "You"), "star_rating": 10,
	"review_body": "So tense and so good, definitely something you can watch in one go"}
	
	you_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "creepy", 
	"show": Show.objects.get(title = "You"), "star_rating": 6,
	"review_body": "This show was kinda creepy and not sure if its in a good way, worth a watch though"}
	
	you_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Tense", 
	"show": Show.objects.get(title = "You"), "star_rating": 8,
	"review_body": "This was super tense at parts, keeps you on edge of your seat"}
	
	bll_review1 = {"reviewer": User.objects.get(username = "thomas"), "title": "Rubbish", 
	"show": Show.objects.get(title = "Big Little Lies"), "star_rating": 3,
	"review_body": "Didnt like this show at all, so I cant recommend anyone watches it"}
	
	bll_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Hate it", 
	"show": Show.objects.get(title = "Big Little Lies"), "star_rating": 2,
	"review_body": "This show wasnt great, it didnt really leave you wanting to watch more"}
	
	bll_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "NOT bingeworthy", 
	"show": Show.objects.get(title = "Big Little Lies"), "star_rating": 2,
	"review_body": "Disappointed in this show, I was expecting to want to binge it"}

	greys_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "So tense", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 7,
	"review_body": "I really liked this, you get very emotionally attatched to the characters"}
	
	greys_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Graphic", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 1,
	"review_body": "You definitely cant be squeamish for this, its super gorey!"}
	
	greys_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Very medical", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 8,
	"review_body": "I found the show really interesting as it seemed to be very medicallu accurate"}
	
	handmaid_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Odd", 
	"show": Show.objects.get(title = "The Handmaids Tale"), "star_rating": 5,
	"review_body": "This show is a bit weird, it was fairly enjoyable though I guess"}
	
	handmaid_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Didnt mind it", 
	"show": Show.objects.get(title = "The Handmaids Tale"), "star_rating": 5,
	"review_body": "Its was okay, i could recommend it if theres no better options"}
	
	handmaid_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Fine", 
	"show": Show.objects.get(title = "The Handmaids Tale"), "star_rating": 5,
	"review_body": "It was something to watch i guess, not great but not terrible"}
	
	peakyBlinders_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Amazing", 
	"show": Show.objects.get(title = "Peaky Blinders"), "star_rating": 8,
	"review_body": "I really loved this show, it was great and I cant wait to watch more"}
	
	peakyBlinders_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Fantastic", 
	"show": Show.objects.get(title = "Peaky Blinders"), "star_rating": 8,
	"review_body": "This show is so gripping and never gets old"}
	
	peakyBlinders_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Brilliant", 
	"show": Show.objects.get(title = "Peaky Blinders"), "star_rating": 8,
	"review_body": "This show really grabs you in, wish i could watch this again for the first time"}
	
	dod_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Haunting", 
	"show": Show.objects.get(title = "Dahmer On Dahmer"), "star_rating": 10,
	"review_body": "This show gives you the chills, very creepy I loved it"}
	
	dod_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Intense", 
	"show": Show.objects.get(title = "Dahmer On Dahmer"), "star_rating": 9,
	"review_body": "This was super intense and eery, would recommend it to anyone interested in this kind of show"}
	
	dod_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Captivating", 
	"show": Show.objects.get(title = "Dahmer On Dahmer"), "star_rating": 9,
	"review_body": "So interesting to really see into the mind of a serial killer"}
	
	htgawm_review1 = {"reviewer": User.objects.get(username = "thomas"), "title": "Watch again", 
	"show": Show.objects.get(title = "How to Get Away with Murder"), "star_rating": 8,
	"review_body": "Something I would watch again, it was a good watch and stayed consistent"}
	
	htgawm_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Good at start", 
	"show": Show.objects.get(title = "How to Get Away with Murder"), "star_rating": 4,
	"review_body": "Show was good at the beginning but wore off in later seasons sadly"}
	
	htgawm_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Good for law", 
	"show": Show.objects.get(title = "How to Get Away with Murder"), "star_rating": 8,
	"review_body": "You would enjoy this a lot if youre studying law, good for everyone though"}
	
	iicb_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Love Ice-T", 
	"show": Show.objects.get(title = "In Ice Cold Blood"), "star_rating": 7,
	"review_body": "Love how the show has Ice T, he keeps it interesting"}
	
	iicb_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Fascinating", 
	"show": Show.objects.get(title = "In Ice Cold Blood"), "star_rating": 7,
	"review_body": "So interesting to hear about the cases and uncovering the mysteries behind them"}
	
	iicb_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Eery", 
	"show": Show.objects.get(title = "In Ice Cold Blood"), "star_rating": 7,
	"review_body": "Some of the cases are pretty dark, dont watch late at night"}
	
	shetland_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Boring", 
	"show": Show.objects.get(title = "Shetland"), "star_rating": 2,
	"review_body": "This show didnt interest me, super boring"}
	
	shetland_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Scottish", 
	"show": Show.objects.get(title = "Shetland"), "star_rating": 6,
	"review_body": "Its quite cool how its filmed in Scotland, nice to see recognisable places"}
	
	shetland_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Cookie cutter crime", 
	"show": Show.objects.get(title = "Shetland"), "star_rating": 2,
	"review_body": "Exactly the same as every crime show on tv, I wouldnt binge it"}
	
	kuwtk_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Guilty pleasure", 
	"show": Show.objects.get(title = "Keeping Up with the Kardashians"), "star_rating": 9,
	"review_body": "I really like this show and you can definitely watch several episodes at a time, good for background watching"}
	
	kuwtk_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Diabolical", 
	"show": Show.objects.get(title = "Keeping Up with the Kardashians"), "star_rating": 1,
	"review_body": "I dont even know why I tried to watch this, its not good"}
	
	kuwtk_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Not sure", 
	"show": Show.objects.get(title = "Keeping Up with the Kardashians"), "star_rating": 6,
	"review_body": "I like it but i also hate it, so im not sure if I can fully recommend it"}
	
	mm_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "So crap", 
	"show": Show.objects.get(title = "Millionaire Matchmaker"), "star_rating": 1,
	"review_body": "This show isnt good, very one dimensional"}
	
	mm_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Worst show", 
	"show": Show.objects.get(title = "Millionaire Matchmaker"), "star_rating": 1,
	"review_body": "This wasnt interesting at all, didnt leave you wanting more"}
	
	mm_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "I hate this", 
	"show": Show.objects.get(title = "Millionaire Matchmaker"), "star_rating": 1,
	"review_body": "Why does this show have so many seasons, you could never binge it"}
	
	apprentice_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Occasional watch", 
	"show": Show.objects.get(title = "The Apprentice"), "star_rating": 5,
	"review_body": "I dont religiously watch this but occasional viewing is okay"}
	
	apprentice_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Unlikeable", 
	"show": Show.objects.get(title = "The Apprentice"), "star_rating": 3,
	"review_body": "I find the people in this show to be super unlikeable which puts me off binging it"}
	
	apprentice_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "Pretty mean", 
	"show": Show.objects.get(title = "The Apprentice"), "star_rating": 5,
	"review_body": "The people on it are pretty mean, but it can still be interesting at times"}
	
	catfish_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Shocking", 
	"show": Show.objects.get(title = "Catfish"), "star_rating": 6,
	"review_body": "So crazy to see the mysterious people be uncovered"}
	
	catfish_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "Sad", 
	"show": Show.objects.get(title = "Catfish"), "star_rating": 6,
	"review_body": "Very interesting show but quite sad to see peoples reactions once the truth is shown"}
	
	catfish_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Crazy", 
	"show": Show.objects.get(title = "Catfish"), "star_rating": 6,
	"review_body": "Its wild to watch the solve these cases"}


	reviews = [office_review1, office_review2, office_review3, office_review4,
	friends_review1, friends_review2, friends_review3, 
	mtw_review1, mtw_review2, mtw_review3, 
	b99_review1, b99_review2, b99_review3,
	community_review1, community_review2, community_review3, 
	strangerThings_review1, strangerThings_review2, strangerThings_review3, 
	docWho_review1, docWho_review2, docWho_review3,
	blackMirror_review1, blackMirror_review2, blackMirror_review3, 
	starTrek_review1, starTrek_review2, starTrek_review3, 
	supernatural_review1, supernatural_review2, supernatural_review3,
	vampDiaries_review1, vampDiaries_review2, vampDiaries_review3, 
	got_review1, got_review2, got_review3, 
	lotr_review1, lotr_review2, lotr_review3, 
	twd_review1, twd_review2, twd_review3,
	mrRobot_review1, mrRobot_review2, mrRobot_review3, 
	luther_review1, luther_review2, luther_review3, 
	you_review1, you_review2, you_review3, 
	bll_review1, bll_review2, bll_review3,
	greys_review1, greys_review2, greys_review3, 
	handmaid_review1, handmaid_review2, handmaid_review3,
	peakyBlinders_review1, peakyBlinders_review2, peakyBlinders_review3, 
	dod_review1, dod_review2, dod_review3, 
	htgawm_review1, htgawm_review2, htgawm_review3, 
	iicb_review1, iicb_review2, iicb_review3, 
	shetland_review1, shetland_review2, shetland_review3, 
	kuwtk_review1, kuwtk_review2, kuwtk_review3, 
	mm_review1, mm_review2, mm_review3, 
	apprentice_review1, apprentice_review2, apprentice_review3, 
	catfish_review1, catfish_review2, catfish_review3]
	
	for review in reviews:
		review_added = add_review(review["reviewer"], review["title"], review["show"], review["star_rating"], review["review_body"])

######################viewership begins here####################################

	
	ajpod_office = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "The Office (US)"), "judgement": True}
	thomas_office = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "The Office (US)"), "judgement": True}
	zeerak_office = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "The Office (US)"), "judgement": True}
	gemma_office = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "The Office (US)"), "judgement": True}
	
	zeerak_friends = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Friends"), "judgement": True}
	thomas_friends = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Friends"), "judgement": True}
	ajpod_friends = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Friends"), "judgement": False}
	
	zeerak_mtw = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Mock the Week"), "judgement": True}
	gemma_mtw = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Mock the Week"), "judgement": True}
	thomas_mtw = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Mock the Week"), "judgement": True}
	
	gemma_b99 = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Brooklyn Nine Nine"), "judgement": True}
	thomas_b99 = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Brooklyn Nine Nine"), "judgement": True}
	ajpod_b99 = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Brooklyn Nine Nine"), "judgement": False}
	
	zeerak_community = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Community"), "judgement": True}
	ajpod_community = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Community"), "judgement": True}
	gemma_community = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Community"), "judgement": True}
	
	gemma_strangerThings = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Stranger Things"), "judgement": True}
	thomas_strangerThings = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Stranger Things"), "judgement": True}
	ajpod_strangerThings = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Stranger Things"), "judgement": True}
	
	ajpod_drWho = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Doctor Who"), "judgement": True}
	zeerak_drWho = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Doctor Who"), "judgement": False}
	thomas_drWho = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Doctor Who"), "judgement": True}
	
	gemma_blackMirror = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Black Mirror"), "judgement": True}
	thomas_blackMirror = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Black Mirror"), "judgement": True}
	zeerak_blackMirror = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Black Mirror"), "judgement": True}
	
	ajpod_starTrek = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Star Trek"), "judgement": True}
	zeerak_starTrek = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Star Trek"), "judgement": False}
	gemma_starTrek = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Star Trek"), "judgement": True}
	
	gemma_supernatural = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Supernatural"), "judgement": True}
	thomas_supernatural = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Supernatural"), "judgement": True}
	zeerak_supernatural = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Supernatural"), "judgement": True}
	
	gemma_vamp = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "The Vampire Diaries"), "judgement": False}
	ajpod_vamp = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "The Vampire Diaries"), "judgement": False}
	thomas_vamp = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "The Vampire Diaries"), "judgement": False}
	
	thomas_got = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Game of Thrones"), "judgement": True}
	zeerak_got = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Game of Thrones"), "judgement": True}
	ajpod_got = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Game of Thrones"), "judgement": True}
	
	ajpod_lotr = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Lord of the Rings"), "judgement": True}
	gemma_lotr = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Lord of the Rings"), "judgement": True}
	thomas_lotr = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Lord of the Rings"), "judgement": True}
	
	ajpod_twd = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "The Walking Dead"), "judgement": True}
	thomas_twd = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "The Walking Dead"), "judgement": True}
	zeerak_twd = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "The Walking Dead"), "judgement": False}
	
	zeerak_mrRobot = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Mr Robot"), "judgement": True}
	thomas_mrRobot = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Mr Robot"), "judgement": True}
	ajpod_mrRobot = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Mr Robot"), "judgement": True}
	
	zeerak_luther = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Luther"), "judgement": False}
	thomas_luther = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Luther"), "judgement": False}
	gemma_luther = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Luther"), "judgement": False}
	
	gemma_you = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "You"), "judgement": True}
	ajpod_you = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "You"), "judgement": True}
	thomas_you = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "You"), "judgement": True}
	
	thomas_bll = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Big Little Lies"), "judgement": False}
	gemma_bll = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Big Little Lies"), "judgement": False}
	zeerak_bll = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Big Little Lies"), "judgement": False}

	gemma_greys = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Grey's Anatomy"), "judgement": True}
	zeerak_greys = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Grey's Anatomy"), "judgement": False}
	ajpod_greys = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Grey's Anatomy"), "judgement": True}
	
	zeerak_handmaid = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "The Handmaids Tale"), "judgement": True}
	gemma_handmaid = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "The Handmaids Tale"), "judgement": True}
	thomas_handmaid = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "The Handmaids Tale"), "judgement": True}
	
	ajpod_peakyBlinders = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Peaky Blinders"), "judgement": True}
	zeerak_peakyBlinders = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Peaky Blinders"), "judgement": True}
	thomas_peakyBlinders = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Peaky Blinders"), "judgement": True}

	gemma_dod = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Dahmer On Dahmer"), "judgement": True}
	ajpod_dod = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Dahmer On Dahmer"), "judgement": True}
	zeerak_dod = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Dahmer On Dahmer"), "judgement": True}

	thomas_htgawm = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "How to Get Away with Murder"), "judgement": True}
	gemma_htgawm = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "How to Get Away with Murder"), "judgement": False}
	ajpod_htgawm = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "How to Get Away with Murder"), "judgement": True}

	zeerak_iicb = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "In Ice Cold Blood"), "judgement": True}
	ajpod_iicb = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "In Ice Cold Blood"), "judgement": True}
	thomas_iicb = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "In Ice Cold Blood"), "judgement": True}

	gemma_shetland = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Shetland"), "judgement": False}
	ajpod_shetland = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Shetland"), "judgement": True}
	zeerak_shetland = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Shetland"), "judgement": False}

	gemma_kuwtk = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Keeping Up with the Kardashians"), "judgement": True}
	ajpod_kuwtk = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Keeping Up with the Kardashians"), "judgement": False}
	zeerak_kuwtk = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Keeping Up with the Kardashians"), "judgement": True}

	ajpod_mm = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Millionaire Matchmaker"), "judgement": False}
	thomas_mm = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Millionaire Matchmaker"), "judgement": False}
	zeerak_mm = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Millionaire Matchmaker"), "judgement": False}
	
	ajpod_apprentice = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "The Apprentice"), "judgement": True}
	gemma_apprentice = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "The Apprentice"), "judgement": False}
	thomas_apprentice = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "The Apprentice"), "judgement": True}

	ajpod_catfish = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "Catfish"), "judgement": True}
	gemma_catfish = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Catfish"), "judgement": True}
	zeerak_catfish = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Catfish"), "judgement": True}
	
	
	
	viewerships = [ajpod_office, thomas_office, zeerak_office, gemma_office,
	zeerak_friends, thomas_friends, ajpod_friends,
	zeerak_mtw, gemma_mtw, thomas_mtw,
	gemma_b99, thomas_b99, ajpod_b99,
	zeerak_community, ajpod_community, gemma_community,
	thomas_strangerThings, ajpod_strangerThings, gemma_strangerThings,
	ajpod_drWho, zeerak_drWho, thomas_drWho,
	gemma_blackMirror, thomas_blackMirror, zeerak_blackMirror,
	ajpod_starTrek, zeerak_starTrek, gemma_starTrek,
	gemma_supernatural, thomas_supernatural, zeerak_supernatural,
	gemma_vamp, ajpod_vamp, thomas_vamp,
	thomas_got, zeerak_got, ajpod_got,
	ajpod_lotr, gemma_lotr, thomas_lotr,
	ajpod_twd, thomas_twd, zeerak_twd,
	zeerak_mrRobot, thomas_mrRobot, ajpod_mrRobot,
	zeerak_luther, thomas_luther, gemma_luther,
	gemma_you, ajpod_you, thomas_you,
	thomas_bll, gemma_bll, zeerak_bll,
	gemma_greys, zeerak_greys, ajpod_greys,
	zeerak_handmaid, gemma_handmaid, thomas_handmaid,
	ajpod_peakyBlinders, zeerak_peakyBlinders, thomas_peakyBlinders,
	gemma_dod, ajpod_dod, zeerak_dod,
	thomas_htgawm, ajpod_htgawm, gemma_htgawm,
	zeerak_iicb, ajpod_iicb, thomas_iicb,
	gemma_shetland, ajpod_shetland, zeerak_shetland,
	gemma_kuwtk, ajpod_kuwtk, zeerak_kuwtk,
	ajpod_mm, thomas_mm, zeerak_mm,
	ajpod_apprentice, gemma_apprentice, thomas_apprentice,
	ajpod_catfish, gemma_catfish, zeerak_catfish
	]
	
	for viewer in viewerships:
		viewer_added = add_viewership(viewer["viewer"], viewer["show"], viewer["judgement"])
		
######################votes on review#######################################

	gem_office_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	gem_office_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	zeerak_office_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	ajpod_office_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": False}
		
	zeerak_office_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	thomas_office_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
		
	ajpod_office_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
	thomas_greys_zee= {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Grey's Anatomy")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
	
	thomas_greys_gem = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Grey's Anatomy")), "voter": User.objects.get(username = "thomas"), 
		"judgement": False}
		
	ajpod_greys_gem = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Grey's Anatomy")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": False}
	
	thomas_vamp_gem = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "The Vampire Diaries")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
		
	ajpod_vamp_gem = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "The Vampire Diaries")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
	zee_vamp_gem = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "The Vampire Diaries")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": False}
		
	gemma_mtw_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Mock the Week")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	gemma_friends_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "Friends")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	gemma_friends_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Friends")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
	
	zeerak_mtw_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Mock the Week")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	zeerak_b99_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Brooklyn Nine Nine")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
	
	zeerak_community_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Community")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	zeerak_community_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "Community")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": False}
		
	gemma_drWho_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "Doctor Who")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	thomas_drWho_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "Doctor Who")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}

	zeerak_bm_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Black Mirror")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	zeerak_bm_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Black Mirror")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}

	zeerak_st_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Star Trek")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	ajpod_st_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Star Trek")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True} 
	
	ajpod_got_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Game of Thrones")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
	thomas_got_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "Game of Thrones")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
	
	ajpod_lotr_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Lord of the Rings")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": False}
		
	ajpod_lotr_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Lord of the Rings")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
	zeerak_lotr_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Lord of the Rings")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	gemma_twd_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "The Walking Dead")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	gemma_twd_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "The Walking Dead")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	thomas_twd_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "The Walking Dead")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
		
	ajpod_luther_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Luther")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
	zeerak_you_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "You")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	ajpod_you_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "You")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
	
	zeerak_you_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "You")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
	
	zeerak_bll_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "Big Little Lies")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	zeerak_bll_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Big Little Lies")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	gemma_handmaid_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "The Handmaids Tale")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	gemma_dod_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Dahmer On Dahmer")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	ajpod_dod_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Dahmer On Dahmer")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
	zeerak_htgawm_thomas = {"review": Review.objects.get(reviewer = User.objects.get(username = "thomas"), 
		show = Show.objects.get(title = "How to Get Away with Murder")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	zeerak_htgawm_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "How to Get Away with Murder")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
		
	thomas_kuwtk_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "Keeping Up with the Kardashians")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
		
	thomas_kuwtk_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Keeping Up with the Kardashians")), "voter": User.objects.get(username = "thomas"), 
		"judgement": False}
		
	thomas_kuwtk_gemma = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Keeping Up with the Kardashians")), "voter": User.objects.get(username = "thomas"), 
		"judgement": False}
		
	thomas_mm_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Millionaire Matchmaker")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
		
	ajpod_mm_zeerak = {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Millionaire Matchmaker")), "voter": User.objects.get(username = "ajpod"), 
		"judgement": True}
		
		
	votes = [gem_office_ajpod, gem_office_thomas, zeerak_office_ajpod, ajpod_office_zeerak, zeerak_office_gemma, thomas_office_gemma, ajpod_office_gemma,
	thomas_greys_zee, thomas_greys_gem, ajpod_greys_gem,
	thomas_vamp_gem, ajpod_vamp_gem, zee_vamp_gem, gemma_mtw_thomas, gemma_friends_ajpod, gemma_friends_zeerak,
	zeerak_mtw_thomas, zeerak_b99_thomas, zeerak_community_gemma, zeerak_community_ajpod, gemma_drWho_ajpod,
	thomas_drWho_ajpod, zeerak_bm_gemma, zeerak_bm_thomas, zeerak_st_gemma, ajpod_st_gemma, ajpod_got_thomas,
	thomas_got_ajpod, ajpod_lotr_thomas, ajpod_lotr_gemma, zeerak_lotr_gemma, gemma_twd_ajpod, gemma_twd_thomas, 
	thomas_twd_ajpod, ajpod_luther_zeerak, zeerak_you_gemma, ajpod_you_gemma, zeerak_you_thomas, zeerak_bll_thomas,
	zeerak_bll_gemma, gemma_handmaid_zeerak, gemma_dod_zeerak, ajpod_dod_zeerak, zeerak_htgawm_thomas, zeerak_htgawm_ajpod, 
	thomas_kuwtk_ajpod, thomas_kuwtk_zeerak,  thomas_kuwtk_gemma, thomas_mm_zeerak, ajpod_mm_zeerak
	]
	
	for vote in votes:
		vote_added = add_vote(vote["review"], vote["voter"], vote["judgement"])
		

################adding to dictionaries################################################
	
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
