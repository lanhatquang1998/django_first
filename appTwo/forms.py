from django import forms
from appTwo.models import User
from django.contrib.auth.models import User
from appTwo.models import UserProfileInfo

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')








# from django.core import validators

# # def check_for(value):
# #     if value[0] != "z":
# #         raise forms.ValidationError("Name need to start with z")    

# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label="Email again")
#     text = forms.CharField(widget=forms.Textarea)
#     # botcatcher = forms.CharField(required=False,
#     #                             widget=forms.HiddenInput,
#     #                             validators=[validators.MaxLengthValidator(0)])

#     def clean(seft):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']

#         if email != vmail:
#             raise forms.ValidationError("make sure email match!")

#     # def clean_botcatcher(self):
#     #     botcatcher = self.cleaned_data['botcatcher']
#     #     if len(botcatcher) > 0:
#     #         raise forms.ValidationError("GOTCHA BOT!")
#     #     return botcatcher