from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BaseForm(forms.Form):
    """
    A base form to apply Bootstrap classes to all fields.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control rounded-pill'})

class SignupForm(BaseForm, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the styling to the custom fields as well
        self.fields['password'].widget.attrs.update({'class': 'form-control rounded-pill'})
        self.fields['password_confirm'].widget.attrs.update({'class': 'form-control rounded-pill'})
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("Email already registered.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password != password_confirm:
            raise ValidationError("Passwords do not match.")

class SigninForm(BaseForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(BaseForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and self.instance and User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
