from django import forms
from Portal.models import Interview, Offer,  Location, Company, Project, Job
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile
from django.utils.translation import ugettext_lazy as _


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        exclude = ["author"]  

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ["author"]

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        
class ProjectForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Project

class JobForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Job

class RegistrationFormZ(forms.Form):
    """
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_("Password (again)"))
    
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']
    
    good_domains = ['cs.unc.edu']
        
    def clean_email(self):
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain not in self.good_domains:
            raise forms.ValidationError(_("Registration using non CS-UNC email addresses is prohibited. Please supply a different email address."))
        else:
            if User.objects.filter(email__iexact=self.cleaned_data['email']):
                raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
            else:
                return self.cleaned_data['email']

def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data
