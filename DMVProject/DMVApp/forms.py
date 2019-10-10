from django.forms import ModelForm
from .models import testModel


class testForm(ModelForm):
    class Meta:
        model = testModel
        fields = '__all__'