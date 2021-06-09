from django import forms

ACCOUNT_TYPES = (
    ('USER','User'), ('DRIVER','Driver')
    )

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100, required=True)
    first_name.widget.attrs.update({'class':'form-control', 'placeholder':'First name'})

    last_name = forms.CharField(label='last_name', max_length=100, required=True)
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder':'Last name'})

    email = forms.EmailField(label='email')
    email.widget.attrs.update({'class': 'form-control', 'placeholder':'Email'})

    phone = forms.CharField(label='phone_number')
    phone.widget.attrs.update({'class': 'form-control', 'placeholder':'Phone number'})

    # label='account_type'

    account_type = forms.ChoiceField(label='account_type', choices= ACCOUNT_TYPES, required=True)
    account_type.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput, required=True)
    password.widget.attrs.update({'class': 'form-control', 'placeholder':'Password'})

    confirm_password = forms.CharField(label='confirm_password', max_length=100, widget=forms.PasswordInput, required=True)
    confirm_password.widget.attrs.update({'class': 'form-control', 'placeholder':'Confirm password'})   
