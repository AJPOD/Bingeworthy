import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bingeworthy_project.settings')

import django
django.setup()
from bingeworthy.models import *

def populate():

	theOffice = {"title": "The Office(US)",
		"genre":"Comedy", "blurb": "A faux docuseries on the lives of workers at a paper company", 
		"starring": "Steve Carell", "platform": "Amazon Prime", "ep_runtime": 20, "num_episodes": 201, 
		"num_season": 9, "year_released": 2005}
	
	shows = [theOffice]
	
	for show in shows:
		show_added = add_show(show["title"], show["genre"], show["blurb"], show["starring"],
			show["platform"], show["ep_runtime"], show["num_episodes"], show["num_season"],
			show["year_released"])
		
	
	user_account = [
	{"username":"testAccount",
	"password":"testpassword"},
	]
	
	viewership = [
	{"viewer":"testAccount",
	"show":"title", "views": 62},
	 ]
	
	cats = {"Python": {"pages": python_pages, "likes":64, "views":128},
	"Django": {"pages": django_pages, "likes": 32, "views":64},
	"Other Frameworks": {"pages": other_pages, "likes":16, "views":32} }
	
	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["likes"], cat_data["views"])
		for p in cat_data["pages"]:
			add_page(c, p["title"], p["url"], p["views"])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))
	
def add_show(title, genre, blurb, starring, platform, ep_runtime, num_episodes, 
num_season, year_released):
	show = Show.objects.get_or_create(title = title, genre = genre, blurb = blurb,
		starring = starring, platform = platform, ep_runtime = ep_runtime, num_episodes = num_episodes,
		num_season = num_season, year_released = year_released)
	show.save()
	return show
	
def add_cat(name, likes, views):
	c = Category.objects.get_or_create(name=name, likes=likes, views=views)[0]
	c.save()
	return c
		
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()