from django import forms
from .models import PrivateMessage


class MessageForm(forms.ModelForm):
	class Meta:
		model = PrivateMessage
		
		fields = ('pmbody',)
		labels = {
           'pmbody' : '',
        }


		widgets = {


		#'title': forms.TextInput(attrs={'class': 'form-control'}),
		#'author': forms.TextInput(attrs={'class': 'form-control'}),
		'pmbody': forms.Textarea(attrs={'minlength': 1,'placeholder': "Write here...",'cols': 30, 'rows': 2,'class': 'form-control'},),
		#'status': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
		#'category': forms.Select(choices=CATEGORY_CHOICES_LIST, attrs={'class': 'form-control'}),


		}
class MessageFormWithUsername(forms.ModelForm):
	class Meta:
		model = PrivateMessage
		
		fields = ('pmreciever','pmbody',)
		labels = {
           'pmbody' : '',
           'pmreciever' : '',

        }


		widgets = {


		'pmreciever': forms.TextInput(attrs={'minlength': 5,'placeholder': "Write Username",'class': 'form-control'}),
		#'author': forms.TextInput(attrs={'class': 'form-control'}),
		'pmbody': forms.Textarea(attrs={'minlength': 1,'placeholder': "Write Message",'cols': 30, 'rows': 2,'class': 'form-control'},),
		#'status': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
		#'category': forms.Select(choices=CATEGORY_CHOICES_LIST, attrs={'class': 'form-control'}),


		}