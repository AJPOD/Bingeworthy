from django import forms 
from django.contrib.auth.models import User
from bingeworthy.models import *

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ReviewForm(forms.ModelForm):
    # title = forms.CharField()
    # star_rating = forms.IntegerField()
    # review_body = forms.CharField()
    class Meta:
        model = Review 
        exclude = ('votes','auto_increment_id','reviewer', 'show',)
        fields = ('title','star_rating','review_body',)
    
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop("user")
    #     super(ReviewForm, self).__init__(*args, **kwargs)