from django.conf.urls import url
from bingeworthy import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.user_login, name='signup'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^contact-us/$', views.contact_us, name='contact_us'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^about-us/$', views.about, name="about"),
    url(r'^search-results/$', views.search_results, name="search_results"),
    url(r'^genres/$', views.genres, name="genres"),
    url(r'^genres/(?P<genre_name_slug>[\w\-]+)/$', views.show_genre, name='show_genre'),
    url(r'^platforms/$', views.platforms, name="platforms"),
    url(r'^platforms/(?P<platform_name_slug>[\w\-]+)/$', views.show_platform, name='show_platform'),
    url(r'^shows/$', views.shows, name="shows"),
    url(r'^shows/top/$', views.shows_top, name="shows_top"),
    url(r'^shows/all/$', views.shows_all, name="shows_all"),
    url(r'^shows/(?P<show_name_slug>[\w\-]+)/$', views.shows_show, name="shows_show"),
    url(r'^shows/(?P<show_name_slug>[\w\-]+)/make-review/$', views.make_review, name="make_review"),
    url(r'^user/profile/(?P<username>[\w\-]+)/$', views.user_profile, name="user_profile"),
    # only using /profile/ because without it, you can't access the my-account
    # as it automatically takes you to the page of the user my-account
    url(r'^user/my-account/$', views.my_account, name='my_account'),
    url(r'^reviews/$', views.show_reviews, name='reviews'),
]
