from django import forms
from .models import User

# Form for registering students, based on the User model
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User  # Link the form to the User model
        fields = ['name', 'email', 'password']  # Specify the fields to be included in the form
        
        # Custom widgets for each field to apply specific HTML attributes for rendering
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',  # Add Bootstrap class for styling
                'autocomplete': 'name',  # HTML autocomplete attribute for name
                'id': 'nameid'  # Custom ID for the name input field
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',  # Add Bootstrap class for styling
                'autocomplete': 'email',  # HTML autocomplete attribute for email
                'id': 'emailid'  # Custom ID for the email input field
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',  # Add Bootstrap class for styling
                'autocomplete': 'new_password',  # HTML autocomplete attribute for new password
                'id': 'passwordid'  # Custom ID for the password input field
            }),
        }
