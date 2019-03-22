from django import forms 
from django.contrib.auth.models import User
from bingeworthy.models import *

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        exclude = ('votes','auto_increment_id','reviewer', 'show',)
        fields = ('title','star_rating','review_body',)