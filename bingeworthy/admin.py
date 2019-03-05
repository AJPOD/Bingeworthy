from django.contrib import admin
from bingeworthy.models import * # sorry was just easier importing all

# Register your models here.
# this stuff lets the admin interface see and interact with models

class ReviewAdmin(admin.ModelAdmin):
    # mainly made this to test upvote_count works -ajpod
    list_display = ('title', 'upvote_count')

class ShowAdmin(admin.ModelAdmin):
    # made to test calculated fields in show
    list_display = ('title', 'views_total', 'star_rating', 'like_ratio')

admin.site.register(UserAccount)
admin.site.register(Show, ShowAdmin)
admin.site.register(Viewership)
admin.site.register(Review, ReviewAdmin)
admin.site.register(VotesOnReview)
