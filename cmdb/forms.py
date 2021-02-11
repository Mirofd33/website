from django.forms import ModelForm
from models import IpSource,Host

class IPsourceForm(ModelForm):
    class Meta:
      model = IpSource
      fields = '__all__'
