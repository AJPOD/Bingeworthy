from django.contrib import admin
from bingeworthy.models import * # sorry was just easier importing all

# Register your models here.
# this stuff lets the admin interface see and interact with models
admin.site.register(UserAccount)
admin.site.register(Show)
admin.site.register(Viewership)
admin.site.register(Review)
admin.site.register(VotesOnReview)
