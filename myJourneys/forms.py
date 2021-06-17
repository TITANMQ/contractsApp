from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _



# account types
ACCOUNT_TYPES = (
    ('USER', _('User') ), ('DRIVER', _('Driver') ))


# code for constructing register forms
class RegisterForm(forms.Form):

    first_name = forms.CharField(label='first_name', max_length=100, required=True)
    first_name.widget.attrs.update({'class':'form-control', 'placeholder':'First name'})

    last_name = forms.CharField(label='last_name', max_length=100, required=True)
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder':'Last name'})

    username = forms.CharField(label='username', max_length=100, required=True)
    username.widget.attrs.update({'class': 'form-control', 'placeholder':'Username'})

    email = forms.EmailField(label='email', required=False)
    email.widget.attrs.update({'class': 'form-control', 'placeholder':'Email'})

    phone = forms.CharField(label='phone_number', required=False)
    phone.widget.attrs.update({'class': 'form-control', 'placeholder':'Phone number'})

    account_type = forms.ChoiceField(label='account_type', choices= ACCOUNT_TYPES, required=True)
    account_type.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput, required=True)
    password.widget.attrs.update({'class': 'form-control', 'placeholder':'Password'})

    confirm_password = forms.CharField(label='confirm_password', max_length=100, widget=forms.PasswordInput, required=True)
    confirm_password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password does not match")
        return confirm_password


# code for constructing booking forms
class BookingForm(forms.Form):
    pick_up = forms.CharField(label='pick_up', max_length=100, required=True)
    pick_up.widget.attrs.update({'class': 'form-control', 'placeholder': 'Pick Up'})

    drop_off = forms.CharField(label='drop_off', max_length=100, required=True)
    drop_off.widget.attrs.update({'class': 'form-control', 'placeholder': 'Drop Off'})

    date = forms.DateField(label='date', required=True, widget=forms.DateInput())
    date.widget.attrs.update({'class': 'form-control', 'placeholder': 'dd/mm/yyyy'})

    time = forms.TimeField(label='time', required=True)
    time.widget.attrs.update({'class': 'form-control', 'placeholder': 'hh:mm'})

    notes = forms.CharField(label='notes', max_length=100, required=False)
    notes.widget.attrs.update({'class': 'form-control', 'placeholder': 'Notes'})

# vehicle types 
VEHICLE_TYPES = (
    ('TUK-TUK','Tuk-tuk'), 
    ('MINI-VAN','Mini van'), 
    ('SPORT-UTILITY VEHICLE','Sport-Utility Vehicle (SUV)'),
    ('CONVERTIBLE','Convertible'), 
    ('COUPE','Coupe')
)

# code for constructing driver registration forms
class DriverRegisterForm(forms.Form):

    vehicle_type = forms.ChoiceField(label='vehicle_type', choices= VEHICLE_TYPES,required=True)
    vehicle_type.widget.attrs.update({'class':'form-control', 'placeholder':'Vehicle type'})

    capacity = forms.IntegerField(label='capacity', max_value=99, required=True)
    capacity.widget.attrs.update({'class': 'form-control', 'placeholder':'Capacity'})

    license_plate = forms.CharField(label='license_plate', max_length=7, required=True)
    license_plate.widget.attrs.update({'class': 'form-control', 'placeholder':'License Plate Code'}) 


# code for constructing login forms
class LoginForm(forms.Form):

    username = forms.CharField(label='username', max_length=100, required=True)
    username.widget.attrs.update({'class': 'form-control', 'placeholder':'Username'})

    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput, required=True)
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

    # def clean_password(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    #     user = authenticate(username=username, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Incorrect password or username provided")
    #     return self.cleaned_data

# code for constructing account forms
class AccountForm(forms.Form):

    first_name = forms.CharField(label='first_name', max_length=100, required=True)
    first_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})

    last_name = forms.CharField(label='last_name', max_length=100, required=True)
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})

    email = forms.EmailField(label='email', max_length=100, required=False)
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})

    phone = forms.CharField(label='phone_number', required=False)
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone number'})

    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput, required=False)
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

    confirm_password = forms.CharField(label='confirm_password', max_length=100, widget=forms.PasswordInput,
                                       required=False)
    confirm_password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

    # error handling to check if password and confirm password are the same
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password does not match")
        return confirm_password


# STATUS_TYPES = (
#     ('ON_GOING', _('On going') ), ('CANCELLED', _('Cancelled')), ('COMPLETED', _('Completed')) )
# class UpdateStatusForm(forms.Form):

#     status = forms.ChoiceField(label='vehicle_type', choices= STATUS_TYPES, required=True)
#     status.widget.attrs.update({'class':'form-control', 'placeholder':'Status'})

