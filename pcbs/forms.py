from django import forms
from .models import Pcb

# Creaet an update form
class UpdateBoard(forms.ModelForm):
    #These things are the same as the model's things.
    part_num = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Part Number'}), required=False)
    rev = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rev'}), required=False)
    serial_num =forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serial Number'}), required=False)
    mac = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'MAC Address'}), required=False)
    ip = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'IP address'}), required=False)
    firmware = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firmware'}), required=False)
    image = forms.ImageField(label='')

    class Meta:
        model = Pcb
        # These fields are the same as the model fields as well
        fields = ('part_num', 'rev', 'serial_num', 'mac', 'ip', 'firmware', 'image', )
