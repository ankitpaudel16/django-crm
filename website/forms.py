from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):

    email = forms.EmailField(Label = "", widget = forms.TextInput(attrs = {'class':'form-control', 'placeholer':'Email Address'}))
    first_name = forms.CharField(Label = "", max_Length = 100, widget = forms.TextInput(attrs = {'class':'form-control', 'placeholer':'First Name'}))
    last_name = forms.CharField(Label = "", max_Length = 100, widget = forms.TextInput(attrs = {'class':'form-control', 'placeholer':'Last Name'}))


    class Meta:
        model = User
        fields  = ('username', 'first_name', 'last_name', 'email','password1', 'password2' )

    def __inti__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class = "form-text text-muted"<small>Required. 150 characters or fewer. Letters, Digits and @/./+/-/_ only </small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Passowrd'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class = "form-text text-muted small"><li>Your Passwrod can\'t be too similar to your personal information.</li><li> Your passwrod must contain at least 8 characters.</li><li> Your password must contain only numerics. </li><li>Your password can\'t be too commonly used password</li></ul> '

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class = "form-text text-muted"><small>Your password must be same as before, for verification. </small></span>'




        