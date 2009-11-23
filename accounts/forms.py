from django import forms
from django.contrib.auth.models import User

from timezones.forms import TimeZoneField

from velocette.accounts.models import Profile

class BaseUserForm(forms.ModelForm):
    username = forms.RegexField(label="Username", max_length=30, regex=r'^\w+$')
    email = forms.EmailField()
    time_zone = TimeZoneField(label="Time Zone", initial='EST')

    class Meta:
        model = User
        fields = ("username","email",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists.")
    
class UserCreationForm(BaseUserForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

            profile = Profile()
            profile.user = user
            profile.time_zone = self.cleaned_data["time_zone"]
            profile.save()
        return user

class ProfileForm(BaseUserForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['time_zone'].initial = self.instance.get_profile().time_zone

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username != self.instance.username:
            return super(ProfileForm, self).clean_username()
        else:
            return username

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        profile = user.get_profile()
        profile.time_zone = self.cleaned_data["time_zone"]
        if commit:
            user.save()
            profile.save()
        return user
