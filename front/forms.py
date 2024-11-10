from django import forms
from .models import Price

#######################################

class AddPrice(forms.ModelForm):

    class Meta:

        model = Price

        fields = '__all__'
        

    # name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':'Enter Service Name'}))
    # price = forms.IntegerField(widget=forms.IntegerField(attrs={'placeholder':'Enter the price'}))