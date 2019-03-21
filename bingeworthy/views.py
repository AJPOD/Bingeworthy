from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from bingeworthy.models import *
from bingeworthy.forms import *

def index(request):
		show = Show.objects.get(slug="the-office-us")
		context_dict = {"featured":show}
		return render(request, 'bingeworthy/index.html', context_dict)

def user_login(request):
	print(request.POST)
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('index'))
	registered = False
        	# copied from rango for now
	# change final line to commented line for proper usage
	context_dict = {}
	if 'login' in request.POST:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse('index'))
				else:
					return HttpResponse("Your Bingeworthy account is disabled.")
			else:
				print("Invalid login details: {0}, {1}".format(username, password))
				return HttpResponse("Invalid login details supplied.")
	elif 'signup' in request.POST:
		
		if request.method == 'POST':
			user_form = UserForm(data = request.POST)

			if user_form.is_valid():
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				registered = True 
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
	else:
		user_form = UserForm()
        #return HttpResponse("TEST login details supplied.")
	return render(request, 'bingeworthy/login.html', {'user_form': user_form, 'registered': registered})


def user_logout(request):
	# PLACEHOLDER - COPIED FROM RANGO
	# Don't think it requires changing
	# Design doesn't show a logout splashscreen, p.inglis says not necessary
	#
	# UPDATE: think there's no need for @login_required
	# as it just returns to index regardless
	#
    logout(request)
    return HttpResponseRedirect(reverse('index'))
	#return HttpResponse("TEST LOGOUT")

def contact_us(request):
	context_dict = {}
	return render(request, 'bingeworthy/contact-us.html', context=context_dict)

def faq(request):
	context_dict = {}
	return render(request, 'bingeworthy/faq.html', context=context_dict)
	
def about(request):
	context_dict = {}
	return render(request, 'bingeworthy/about-us.html', context=context_dict)

def search_results(request):
	# not sure how we're going to do this one
	query = request.POST.get('query')
	if query == "" or query.isspace():
		return render(request, 'bingeworthy/search.html', context={})
	results = []
	tempResults = Show.objects.filter(title__icontains=query)
	results = addToResults(results,tempResults)
	tempResults = Show.objects.filter(starring__icontains=query)
	results = addToResults(results,tempResults)
	tempResults = Show.objects.filter(blurb__icontains=query)
	results = addToResults(results,tempResults)
	try:
		tempResults = Show.objects.filter(year_released=int(query))
		results = addToResults(results,tempResults)
	except:
		pass
	return render(request, 'bingeworthy/search.html', context={'results': results, 'query': query})

def addToResults(results, tempResults): # helper method for adding to search results, keeps it cleaner
	for r in tempResults:
		if r not in results:
			results.append(r)
	return results

def genres(request):
	genre_list = Genre.objects.all()
	shows_list = Show.objects.order_by('-genre')
	
	context_dict = {'genres': genre_list, 'shows':shows_list}
	return render(request, 'bingeworthy/genres.html', context_dict)

def show_genre(request, genre_name_slug):
	# can confirm it works, for now just makeup a variable in the url for the name
	return HttpResponse("TEST GENRE PAGE " + genre_name_slug)

def platforms(request):
	platform_list = Platform.objects.all()
	shows_list = Show.objects.order_by('-platform')
	
	context_dict = {'platform': platform_list, 'shows':shows_list}
	return render(request, 'bingeworthy/platforms.html', context_dict)

def show_platform(request, platform_name_slug):
	# see show_genre
	return HttpResponse("TEST PLATFORM PAGE " + platform_name_slug)

def shows(request):
	shows_list = Show.objects.order_by('-title')
	context_dict = {'shows': shows_list}
	return render(request, 'bingeworthy/shows.html', context_dict)

def shows_top(request):
	shows_list = Show.objects.all()
	rating_dict = {}
	for show in shows_list:
		rating_dict[show] = show.like_ratio
	
	sorted_rating_list = sorted(rating_dict,key=rating_dict.__getitem__,reverse=True)
	new_shows_list = sorted_rating_list[:10]
	context_dict = {'shows': new_shows_list}
	return render(request, 'bingeworthy/shows-top.html', context_dict)

def shows_all(request):
	shows_list = Show.objects.order_by('-title')
	context_dict = {'shows': shows_list}
	return render(request, 'bingeworthy/shows-all', context_dict)

def shows_show(request, show_name_slug):
	print(request.POST)
	if 'like.x' in request.POST:
		if request.method == 'POST':
			if not request.user.is_authenticated():
				return HttpResponseRedirect(reverse('login'))
			likeOrDislike(True, request, show_name_slug)
	if 'dislike.x' in request.POST:
		if request.method == 'POST':
			if not request.user.is_authenticated():
				return HttpResponseRedirect(reverse('login'))
			likeOrDislike(False, request, show_name_slug)	
	if 'upvote.x' in request.POST:
		if request.method == 'POST':
			if not request.user.is_authenticated():
				return HttpResponseRedirect(reverse('login'))
			vote(True, request, show_name_slug)
	elif 'downvote.x' in request.POST:
		if request.method == 'POST':
			if not request.user.is_authenticated():
				return HttpResponseRedirect(reverse('login'))
			vote(False, request, show_name_slug)
	context_dict = {}
	good_items = []
	try:
		show = Show.objects.get(slug=show_name_slug)
		reviews = Review.objects.filter(show=show)
		shows_like_this = Show.objects.filter(genre=show.genre)
		context_dict['show'] = show 
		context_dict['reviews'] = reviews
		for item in shows_like_this:
			if item != show:
				good_items.append(item)
		context_dict['show1'] = good_items[0]
		context_dict['show2'] = good_items[1]
		context_dict['show3'] = good_items[2]
		context_dict['star_rating'] = show.star_rating
		context_dict['like_ratio'] = show.like_ratio
		try:
			viewed = Viewership.objects.get(viewer=request.user, show=show)
		except:
			viewed = None 
		context_dict['viewed'] = viewed
	except Show.DoesNotExist:
		context_dict['show'] = None 
		context_dict['reviews'] = None 

	return render(request, 'bingeworthy/show.html', context_dict)

def vote(vote, request, show): #helper method for upvoting etc
	print(request.user.username)
	reviewer = request.POST.get('author')
	try: # voteObject is just temporary object, need to change the full thing for it to work
		voteObject = VotesOnReview.objects.get(voter = User.objects.get(username=request.user.username), review = Review.objects.get(reviewer = User.objects.get(username=reviewer), show = Show.objects.get(slug=show)))
		if voteObject.judgement == vote: # if vote is same as already voted, delete vote
			VotesOnReview.objects.get(voter = User.objects.get(username=request.user.username), review = Review.objects.get(reviewer = User.objects.get(username=reviewer), show = Show.objects.get(slug=show))).delete()
		else: # if vote is different to previous, record is set as new vote
			voteObject.judgement = vote
			voteObject.save()
		return  # i'm sorry about all this, i truly am
	except VotesOnReview.DoesNotExist: # don't hurt me, it's just the way the models cookie crumbled and they've already hurt me more than any human could
		VotesOnReview.objects.create(voter = User.objects.get(username=request.user.username), review = Review.objects.get(reviewer = User.objects.get(username=reviewer), show = Show.objects.get(slug=show)), judgement = vote)
		return

def likeOrDislike(vote, request, show):
	try:
		voteObject = Viewership.objects.get(viewer=request.user, show=Show.objects.get(slug=show))
		voteObject.judgement = vote
		voteObject.save()
		return
	except Viewership.DoesNotExist:
		Viewership.objects.create(viewer=request.user, show=Show.objects.get(slug=show), judgement = vote)
		return






def make_review(request, show_name_slug):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('login'))
	try:
		show = Show.objects.get(slug=show_name_slug)
	except Show.DoesNotExist:
		show = None
	try:
		alreadyReviewed = Review.objects.get(reviewer=request.user, show=show)
	except:
		alreadyReviewed = None
	try:
		viewershipCheck = Viewership.objects.get(viewer=request.user, show=show)
	except:
		viewershipCheck = None
	review_form = ReviewForm()
	context_dict = {'show': show, 'alreadyReviewed': alreadyReviewed, 'viewershipCheck': viewershipCheck}
	if request.method == 'POST':
		review_form = ReviewForm(request.POST, request.user, show)
		review_title = request.POST.get('title')
		review_body = request.POST.get('review_body')
		review_stars = request.POST.get('star_rating')
		
		if review_form.is_valid():
			review = Review() # if the review form is correct, make a new review object 
			review.reviewer = request.user # as its now safe to put that data in the new object
			review.show = show # long story why only this works, much late night
			review.review_body = review_body
			review.title = review_title
			review.star_rating = review_stars

			review.save()
			return HttpResponseRedirect(reverse('shows_show', kwargs={'show_name_slug': show.slug}))
		else:
			print(review_form.as_ul())
			return HttpResponse("Something went wrong :(")


	return render(request, 'bingeworthy/make_review.html', context_dict)

def user_profile(request, username):
	# see show_genre

	try:
		user = User.objects.get(username=username)
		shows_watched = Viewership.objects.filter(viewer_id=user)
		reviews = Review.objects.filter(reviewer=user)
		
		context_dict = {'user': user, 'shows_watched': shows_watched, 'reviews': reviews}
	except User.DoesNotExist:
		context_dict = {'user': None, 'shows_watched': None, 'reviews': None}
	
	return render(request, 'bingeworthy/user-profile.html', context_dict)
	# return HttpResponse("TEST USER PROFILE OF " + username)


def my_account(request):
	return HttpResponse("TEST MY ACCOUNT")

def show_reviews(request):
	print(request.POST)
	if 'upvote.x' in request.POST:
		if request.method == 'POST':
			if not request.user.is_authenticated():
				return HttpResponseRedirect(reverse('login'))
			vote(True, request, request.POST.get("showname"))
	elif 'downvote.x' in request.POST:
		if request.method == 'POST':
			if not request.user.is_authenticated():
				return HttpResponseRedirect(reverse('login'))
			vote(False, request, request.POST.get("showname"))
	context_dict = {}
	good_items = []
	reviews_list = Review.objects.order_by('-title')
	context_dict = {"reviews":reviews_list}
	return render(request, 'bingeworthy/reviews.html', context=context_dict)


