from re import A
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import PostApplication, PostRecruit, PostProfile
from django.contrib.auth.models import User
from .models import PostRecruit


class PostForm(forms.ModelForm):
    class Meta:
        model = PostRecruit
        fields = ('song', 'parts', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class PostApplicationForm(forms.ModelForm):
    class Meta:
        model = PostApplication
        fields = ('a_parts', 'a_comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PostProfileForm(forms.ModelForm):
    class Meta:
        model = PostProfile
        fields = ('introduction','p_part','sex','high','middle','low','freetime')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



class SearchForm(forms.Form):
    freeword = forms.CharField(min_length=1,max_length=30, label='', required=False)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


# class SearchMyProfileForm(forms.ModelForm):
#     freeword = User.username
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
