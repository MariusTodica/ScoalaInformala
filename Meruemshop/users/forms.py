
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from files.upload import store_uploaded_file
from users.models import Profile

AuthUser = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']

    password = forms.CharField(
        max_length=255,
        required=True,
        label='Password',
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html()
    )

    password_confirmation = forms.CharField(
        max_length=255,
        required=True,
        label='Confirm password',
        widget=forms.PasswordInput,
        help_text='Please confirm your password'
    )

    def clean_password(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        # username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = AuthUser(
            first_name=first_name,
            last_name=last_name,
            # username=username
        )

        validate_password(password, user=user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('Password not confirmed.')

        return password_confirmation

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        self.instance.set_password(password)

        return super().save(commit)


class UserImageForm(forms.Form):
    image = forms.ImageField(label='Image to upload', required=True)

    def save(self):
        image = self.cleaned_data.get('image')
        store_uploaded_file(image)


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
