from django.forms import forms,ModelForm
from .models import *
from django.forms.models import inlineformset_factory


class BannerForm(ModelForm):
    class Meta:
        model = Banner
        exclude = ('created_by','modify_by')


    def __init__(self, *args, **kwargs):
        super(BannerForm, self).__init__(*args, **kwargs)
        self.fields['banner_name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
