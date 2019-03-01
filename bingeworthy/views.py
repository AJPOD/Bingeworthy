from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("TEST INDEX")

def user_login(request):
	# PLACEHOLDER - COPIED FROM RANGO
	# 
	# Not sure exactly what needs changed, original design has both login
	# and signup on same page, login and signup URLs both point to this view for now
	#
	# if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(username=username, password=password)

    #     if user:
    #         if user.is_active:
    #             login(request, user)
    #             return HttpResponseRedirect(reverse('index'))
    #         else:
    #             return HttpResponse("Your Bingeworthy account is disabled.")
    #     else:
    #         print("Invalid login details: {0}, {1}".format(username, password))
    #         return HttpResponse("Invalid login details supplied.")
    # else:
    #     return render(request, 'rango/login.html', {})
	return HttpResponse("TEST LOGIN")


def user_logout(request):
	# PLACEHOLDER - COPIED FROM RANGO
	# Don't think it requires changing
	# Design doesn't show a logout splashscreen, p.inglis says not necessary
	#
	# logout(request)
    # return HttpResponseRedirect(reverse('index'))
	return HttpResponse("TEST LOGOUT")

def contact_us(request):
	return HttpResponse("TEST CONTACT US")

def faq(request):
	return HttpResponse("TEST FAQ")

def about(request):
	return HttpResponse("TEST ABOUT")

def search_results(request):
	# not sure how we're going to do this one
	return HttpResponse("TEST SEARCH RESULTS")

def genres(request):
	return HttpResponse("TEST GENRES")

def show_genre(request, genre_name_slug):
	# can confirm it works, for now just makeup a variable in the url for the name
	return HttpResponse("TEST GENRE PAGE " + genre_name_slug)

def platforms(request):
	return HttpResponse("TEST PLATFORMS")

def show_platform(request, platform_name_slug):
	# see show_genre
	return HttpResponse("TEST PLATFORM PAGE " + platform_name_slug)

def shows(request):
	return HttpResponse("TEST SHOWS")

def shows_top(request):
	return HttpResponse("TEST TOP SHOWS")

def shows_all(request):
	return HttpResponse("TEST ALL SHOWS")

def shows_show(request, show_name_slug):
	return HttpResponse("TEST SHOW PAGE " + show_name_slug)

def make_review(request, show_name_slug):
	return HttpResponse("TEST MAKE REVIEW OF " + show_name_slug)

def user_profile(request, username):
	# see show_genre
	return HttpResponse("TEST USER PROFILE OF " + username)

def my_account(request):
	return HttpResponse("TEST MY ACCOUNT")


