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
		
	mockTheWeek = {"title": "Mock the Week", "genre":Genre.objects.get(genre = "Comedy"), 
		"blurb": "A British, satirical celebrity panel show, where comedians discuss the news events from the week.", 
		"starring": "Dara O'Briain", "platform": Platform.objects.get(platform = "BBC iPlayer"), "ep_runtime": 30, "num_episodes": 188, 
		"num_season": 17, "year_released": 2005}
		
	brooklynNineNine = {"title": "Brooklyn Nine Nine", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "Follow the happy-go-lucky detective, Jake Peralta, in his shenanigans in New York with his precinct.", 
		"starring": "Andy Samberg", "platform": Platform.objects.get(platform = "Netflix"), 
		"ep_runtime": 20, "num_episodes": 122, "num_season": 6, "year_released": 2013}
		
	community = {"title": "Community", "genre": Genre.objects.get(genre = "Comedy"), 
		"blurb": "A group of misfits become friends as the study at Greendale Community College", 
		"starring": "Joel McHale", "platform": Platform.objects.get(platform = "Amazon Prime"), 
		"ep_runtime": 20, "num_episodes": 110, "num_season": 6, "year_released": 2015}
		
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
		"blurb": "Detective helps Steland police solve a myterious murder.", 
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
	
	shows = [theOffice, friends, mockTheWeek, brooklynNineNine, community,
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
	
	b99_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "great characters", 
	"show": Show.objects.get(title = "Brooklyn Nine Nine"), "star_rating": 8,
	"review_body": "Characters are really funny"}
	
	b99_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "doesnt dry up", 
	"show": Show.objects.get(title = "Brooklyn Nine Nine"), "star_rating": 7,
	"review_body": "With shows like this they can dry up but this stays funny"}
	
	b99_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "dont like it", 
	"show": Show.objects.get(title = "Brooklyn Nine Nine"), "star_rating": 2,
	"review_body": "i didnt fiind it very funny to be honest"}
	
	community_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "its alright", 
	"show": Show.objects.get(title = "Community"), "star_rating": 5,
	"review_body": "Its not the best, not the worst"}
	
	community_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "love it", 
	"show": Show.objects.get(title = "Community"), "star_rating": 10,
	"review_body": "This show is great, exactly what ive been looking for"}
	
	community_review3 = {"reviewer": User.objects.get(username = "gemma"), "title": "surprisingly good", 
	"show": Show.objects.get(title = "Community"), "star_rating": 7,
	"review_body": "Didnt think id like it but it was actually really funny"}

	strangerThings_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "great theme", 
	"show": Show.objects.get(title = "Stranger Things"), "star_rating": 7,
	"review_body": "Really good show but the theme is just perfection"}
	
	strangerThings_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "scary enough", 
	"show": Show.objects.get(title = "Stranger Things"), "star_rating": 7,
	"review_body": "Its a good level of scary without being horror"}
	
	strangerThings_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "80s era", 
	"show": Show.objects.get(title = "Stranger Things"), "star_rating": 8,
	"review_body": "its set in the 80s which i love"}
	
	docWho_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "my favourite", 
	"show": Show.objects.get(title = "Doctor Who"), "star_rating": 10,
	"review_body": "All time favourite show"}
	
	docWho_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "hate it", 
	"show": Show.objects.get(title = "Doctor Who"), "star_rating": 1,
	"review_body": "Only good if youre into old shows"}
	
	docWho_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "weird", 
	"show": Show.objects.get(title = "Doctor Who"), "star_rating": 6,
	"review_body": "First time watching an old show but its not too bad"}
	
	blackMirror_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "eye opening", 
	"show": Show.objects.get(title = "Black Mirror"), "star_rating": 9,
	"review_body": "Really makes you think"}
	
	blackMirror_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "disturbing", 
	"show": Show.objects.get(title = "Black Mirror"), "star_rating": 6,
	"review_body": "Quite haunting"}
	
	blackMirror_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "so cool", 
	"show": Show.objects.get(title = "Black Mirror"), "star_rating": 9,
	"review_body": "Never seen a show like this"}
	
	starTrek_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "good for an old show", 
	"show": Show.objects.get(title = "Star Trek"), "star_rating": 7,
	"review_body": "Not as good as doctor who but alright"}
	
	starTrek_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "new one is better",
	"show": Show.objects.get(title = "Star Trek"), "star_rating": 6,
	"review_body": "Its okay but the newer version is better"}
	
	starTrek_review3 = {"reviewer": User.objects.get(username = "gemma"), "title": "old school", 
	"show": Show.objects.get(title = "Star Trek"), "star_rating": 7,
	"review_body": "Its an old show but its still good to watch"}

	supernatural_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "So good", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 10,
	"review_body": "I loved this show, its action filled and scary too"}
	
	supernatural_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "Scary", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 5,
	"review_body": "Think this is a bit too dark for me, the characters were likable though"}

	supernatural_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "its meh", 
	"show": Show.objects.get(title = "Supernatural"), "star_rating": 6,
	"review_body": "Similar to other shows in the same vein"}
	
	vampDiaries_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "Too angsty", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 3,
	"review_body": "The dialogue in this is pretty bad and the storyline is predictable"}
	
	vampDiaries_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "Twilight-y", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 0,
	"review_body": "Its made for teens, if you enjoyed Twilight then youd like this."}
	
	vampDiaries_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "this is bad", 
	"show": Show.objects.get(title = "The Vampire Diaries"), "star_rating": 1,
	"review_body": "Really easy to get bored of it"}
	
	got_review1 = {"reviewer": User.objects.get(username = "thomas"), "title": "best show ever", 
	"show": Show.objects.get(title = "Game of Thrones"), "star_rating": 10,
	"review_body": "This is one of the best shows ive ever seen"}
	
	got_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "middle seasons arent great", 
	"show": Show.objects.get(title = "Game of Thrones"), "star_rating": 8,
	"review_body": "seasons in the middle arent great but its gets better recently"}
	
	got_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "this is everything", 
	"show": Show.objects.get(title = "Game of Thrones"), "star_rating": 10,
	"review_body": "This show is just everything"}
	
	lotr_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "not out yet", 
	"show": Show.objects.get(title = "Lord of the Rings"), "star_rating": 9,
	"review_body": "Not out yet but i know its gonna be good"}
	
	lotr_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "excited to try it", 
	"show": Show.objects.get(title = "Lord of the Rings"), "star_rating": 8,
	"review_body": "Im not a diehard fan but im excited to see this"}
	
	lotr_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "hyped", 
	"show": Show.objects.get(title = "Lord of the Rings"), "star_rating": 9,
	"review_body": "So hyped for this to come out in 2020"}

	twd_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "good", 
	"show": Show.objects.get(title = "The Walking Dead"), "star_rating": 9,
	"review_body": "Really liked this"}
	
	twd_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "gorey", 
	"show": Show.objects.get(title = "The Walking Dead"), "star_rating": 9,
	"review_body": "pretty gorey but still really great"}
	
	twd_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "stopped watching", 
	"show": Show.objects.get(title = "The Walking Dead"), "star_rating": 6,
	"review_body": "Sort of lost interest after a while"}
	
	mrRobot_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "show lead was great", 
	"show": Show.objects.get(title = "Mr Robot"), "star_rating": 7,
	"review_body": "Really liked the starring actor"}
	
	mrRobot_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "acting was great", 
	"show": Show.objects.get(title = "Mr Robot"), "star_rating": 7,
	"review_body": "The acting was really great in this show"}
	
	mrRobot_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "rami malek", 
	"show": Show.objects.get(title = "Mr Robot"), "star_rating": 7,
	"review_body": "Rami malek is such a great actor"}
	
	luther_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "its meh", 
	"show": Show.objects.get(title = "Luther"), "star_rating": 4,
	"review_body": "Similar to many crime shows"}
	
	luther_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "predictable", 
	"show": Show.objects.get(title = "Luther"), "star_rating": 4,
	"review_body": "Youu kinda know whats going to happen in it"}
	
	luther_review3 = {"reviewer": User.objects.get(username = "gemma"), "title": "didnt like it", 
	"show": Show.objects.get(title = "Luther"), "star_rating": 4,
	"review_body": "Its not very good to be honest"}
	
	you_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "sooo good", 
	"show": Show.objects.get(title = "You"), "star_rating": 10,
	"review_body": "So tense and so good, definitely something you can watch in one go"}
	
	you_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "creepy", 
	"show": Show.objects.get(title = "You"), "star_rating": 6,
	"review_body": "This show was kinda creepy and not in a good way"}
	
	you_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "tense", 
	"show": Show.objects.get(title = "You"), "star_rating": 8,
	"review_body": "This was super tense at parts, keeps you on edge of your seat"}
	
	bll_review1 = {"reviewer": User.objects.get(username = "thomas"), "title": "rubbish", 
	"show": Show.objects.get(title = "Big Little Lies"), "star_rating": 3,
	"review_body": "Didnt like this show at all"}
	
	bll_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "hate it", 
	"show": Show.objects.get(title = "Big Little Lies"), "star_rating": 2,
	"review_body": "This show was so bad"}
	
	bll_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "terrible", 
	"show": Show.objects.get(title = "Big Little Lies"), "star_rating": 2,
	"review_body": "everything about this show was bad"}

	greys_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "So tense", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 7,
	"review_body": "I really liked this, you get very emotionally attatched to the characters"}
	
	greys_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "Graphic", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 1,
	"review_body": "You definitely cant be squeamish for this, its super gorey!"}
	
	greys_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "very medical", 
	"show": Show.objects.get(title = "Grey's Anatomy"), "star_rating": 8,
	"review_body": "Interesting because it is very medical"}
	
	handmaid_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "odd", 
	"show": Show.objects.get(title = "The Handmaids Tale"), "star_rating": 5,
	"review_body": "This show is a bit weird"}
	
	handmaid_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "didnt mind it", 
	"show": Show.objects.get(title = "The Handmaids Tale"), "star_rating": 5,
	"review_body": "Its was okay, i could recommend it"}
	
	handmaid_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "fine", 
	"show": Show.objects.get(title = "The Handmaids Tale"), "star_rating": 5,
	"review_body": "It was something to watch i guess"}
	
	peakyBlinders_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "amazing", 
	"show": Show.objects.get(title = "Peaky Blinders"), "star_rating": 8,
	"review_body": "really lovde this show it was great"}
	
	peakyBlinders_review2 = {"reviewer": User.objects.get(username = "zeerak"), "title": "fantastic", 
	"show": Show.objects.get(title = "Peaky Blinders"), "star_rating": 8,
	"review_body": "this show is so gripping"}
	
	peakyBlinders_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "brilliant", 
	"show": Show.objects.get(title = "Peaky Blinders"), "star_rating": 8,
	"review_body": "This show really grabbs you in, would binge this again if i could"}
	
	dod_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "haunting", 
	"show": Show.objects.get(title = "Dahmer On Dahmer"), "star_rating": 10,
	"review_body": "This show gives you the chills"}
	
	dod_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "intense", 
	"show": Show.objects.get(title = "Dahmer On Dahmer"), "star_rating": 9,
	"review_body": "This was super intense and eery"}
	
	dod_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "captivating", 
	"show": Show.objects.get(title = "Dahmer On Dahmer"), "star_rating": 9,
	"review_body": "So interesting to really see into the mind of a serial killer"}
	
	htgawm_review1 = {"reviewer": User.objects.get(username = "thomas"), "title": "watch again", 
	"show": Show.objects.get(title = "How to Get Away with Murder"), "star_rating": 8,
	"review_body": "Something i would watch again"}
	
	htgawm_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "good at start", 
	"show": Show.objects.get(title = "How to Get Away with Murder"), "star_rating": 5,
	"review_body": "SHow was good at the beginning but wore off in later seasons"}
	
	htgawm_review3 = {"reviewer": User.objects.get(username = "ajpod"), "title": "good for law", 
	"show": Show.objects.get(title = "How to Get Away with Murder"), "star_rating": 8,
	"review_body": "Youd enjoy this a lot if youre studying law"}
	
	iicb_review1 = {"reviewer": User.objects.get(username = "zeerak"), "title": "love ice t", 
	"show": Show.objects.get(title = "In Ice Cold Blood"), "star_rating": 7,
	"review_body": "Love how the show has Ice T"}
	
	iicb_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "fascinating", 
	"show": Show.objects.get(title = "In Ice Cold Blood"), "star_rating": 7,
	"review_body": "So interesting to hear about the cases"}
	
	iicb_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "eery", 
	"show": Show.objects.get(title = "In Ice Cold Blood"), "star_rating": 7,
	"review_body": "Some f the cases are pretty dark"}
	
	shetland_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "boring", 
	"show": Show.objects.get(title = "Shetland"), "star_rating": 2,
	"review_body": "This show didnt interest me, super boring"}
	
	shetland_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "scottish", 
	"show": Show.objects.get(title = "Shetland"), "star_rating": 6,
	"review_body": "Its quite cool how its filmed in Scotland, nice to see recognisable places"}
	
	shetland_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "cookie cutter crime", 
	"show": Show.objects.get(title = "Shetland"), "star_rating": 2,
	"review_body": "Exactly the same as every crime show on tv"}
	
	kuwtk_review1 = {"reviewer": User.objects.get(username = "gemma"), "title": "guilty pleasure", 
	"show": Show.objects.get(title = "Keeping Up with the Kardashians"), "star_rating": 9,
	"review_body": "Ashamed to admit i really like this show, good for background watching"}
	
	kuwtk_review2 = {"reviewer": User.objects.get(username = "ajpod"), "title": "diabolical", 
	"show": Show.objects.get(title = "Keeping Up with the Kardashians"), "star_rating": 1,
	"review_body": "I dont even know why i tried to watch this"}
	
	kuwtk_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "idk", 
	"show": Show.objects.get(title = "Keeping Up with the Kardashians"), "star_rating": 6,
	"review_body": "I like it but i also hate it"}
	
	mm_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "so crap", 
	"show": Show.objects.get(title = "Millionaire Matchmaker"), "star_rating": 1,
	"review_body": "This is so bad do not watch this show"}
	
	mm_review2 = {"reviewer": User.objects.get(username = "thomas"), "title": "worst show", 
	"show": Show.objects.get(title = "Millionaire Matchmaker"), "star_rating": 1,
	"review_body": "This is the worst show ive ever seen"}
	
	mm_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "i hate this", 
	"show": Show.objects.get(title = "Millionaire Matchmaker"), "star_rating": 1,
	"review_body": "Why does this show have so many seasons"}
	
	apprentice_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "occasional watch", 
	"show": Show.objects.get(title = "The Apprentice"), "star_rating": 5,
	"review_body": "I dont religiously watch this but occasional viewing is okay"}
	
	apprentice_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "unlikeable", 
	"show": Show.objects.get(title = "The Apprentice"), "star_rating": 3,
	"review_body": "I find the people in this show to be super unlikeable"}
	
	apprentice_review3 = {"reviewer": User.objects.get(username = "thomas"), "title": "pretty mean", 
	"show": Show.objects.get(title = "The Apprentice"), "star_rating": 5,
	"review_body": "It can be quite a mean show for the people who are in it"}
	
	catfish_review1 = {"reviewer": User.objects.get(username = "ajpod"), "title": "shocking", 
	"show": Show.objects.get(title = "Catfish"), "star_rating": 6,
	"review_body": "So crazy what people will do to get someone to date them"}
	
	catfish_review2 = {"reviewer": User.objects.get(username = "gemma"), "title": "sad", 
	"show": Show.objects.get(title = "Catfish"), "star_rating": 6,
	"review_body": "Quite sad to see what causes people to act like that"}
	
	catfish_review3 = {"reviewer": User.objects.get(username = "zeerak"), "title": "crazy", 
	"show": Show.objects.get(title = "Catfish"), "star_rating": 6,
	"review_body": "Its wild how far people take these schemes"}


	reviews = [office_review1, office_review2, office_review3, 
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
	gemma_greys = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Grey's Anatomy"), "judgement": True}
	zeerak_greys = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Grey's Anatomy"), "judgement": False}
	zeerak_friends = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Friends"), "judgement": True}
	thomas_friends = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Friends"), "judgement": True}
	gemma_supernatural = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Supernatural"), "judgement": True}
	thomas_supernatural = {"viewer": User.objects.get(username = "thomas"), "show": Show.objects.get(title = "Supernatural"), "judgement": True}
	gemma_vamp = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "The Vampire Diaries"), "judgement": False}
	ajpod_vamp = {"viewer": User.objects.get(username = "ajpod"), "show": Show.objects.get(title = "The Vampire Diaries"), "judgement": False}
	zeerak_mtw = {"viewer": User.objects.get(username = "zeerak"), "show": Show.objects.get(title = "Mock the Week"), "judgement": True}
	gemma_mtw = {"viewer": User.objects.get(username = "gemma"), "show": Show.objects.get(title = "Mock the Week"), "judgement": True}
	
	
	viewerships = [ajpod_office, thomas_office, gemma_greys, zeerak_greys,
		zeerak_friends, thomas_friends, gemma_supernatural, thomas_supernatural,
		gemma_vamp, ajpod_vamp, zeerak_mtw, gemma_mtw]
	
	for viewer in viewerships:
		viewer_added = add_viewership(viewer["viewer"], viewer["show"], viewer["judgement"])
		
######################votes on review#######################################

	gem_office_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "gemma"), 
		"judgement": True}
		
	zee_office_ajpod = {"review": Review.objects.get(reviewer = User.objects.get(username = "ajpod"), 
		show = Show.objects.get(title = "The Office (US)")), "voter": User.objects.get(username = "zeerak"), 
		"judgement": True}
	
	thomas_greys_zee= {"review": Review.objects.get(reviewer = User.objects.get(username = "zeerak"), 
		show = Show.objects.get(title = "Grey's Anatomy")), "voter": User.objects.get(username = "thomas"), 
		"judgement": True}
	
	thomas_greys_gem = {"review": Review.objects.get(reviewer = User.objects.get(username = "gemma"), 
		show = Show.objects.get(title = "Grey's Anatomy")), "voter": User.objects.get(username = "thomas"), 
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
	
	votes = [gem_office_ajpod, zee_office_ajpod, thomas_greys_zee, thomas_greys_gem,
	thomas_vamp_gem, ajpod_vamp_gem, zee_vamp_gem]
	
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
