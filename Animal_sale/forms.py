
from django import forms

from .models import Contact,Buy


class ContactUs(forms.ModelForm):
    class Meta:
        model=Contact

        fields=['FirstName','MiddelName','LastName','Password','Email','Phone','Address']

        widgets={
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),

            'MiddelName':forms.TextInput(attrs={'class':'form-control'}),

            'LastName':forms.TextInput(attrs={'class':'form-control'}),

            'Password':forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
        }

class BuyHere(forms.ModelForm):
    class Meta:
        model=Buy

        fields=['AnimalCategory','AnimalBreed','YourName','Phone','Email','Quntity','Pricepercattle','Pincode','BuyWithin','description']

        widgets={
            'Animal Category':forms.TextInput(attrs={'class':'form-control'}),

            'Animal Breed':forms.TextInput(attrs={'class':'form-control'}),

            'YourName':forms.TextInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            
            'Quntity to Purchase':forms.TextInput(attrs={'class':'form-control'}),
            'Price Per Cattle':forms.ChoiceField(),
            'Pincode':forms.TextInput(attrs={'class':'form-control'}),

            'Buy Within':forms.ChoiceField(),
            'description':forms.TextInput(attrs={'class':'form-control'}),


        }