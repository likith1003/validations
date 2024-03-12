from django import forms

def validator_for_a(data):
    if data[0]in'aA':
        raise forms.ValidationError('Invalid Data')


def validator_for_len(data):
    if len(data)<=5:
        raise forms.ValidationError('Invalid Data')
    
g = [['MALE', 'Male'], ["FEMALE", 'Female']]
c = [['Python', 'PYTHON'], ['Sql', 'SQL'], ['Django', 'DJANGO']]

class StudentForm(forms.Form):
    sname = forms.CharField(max_length=50, required=False, validators=[validator_for_a, validator_for_len])
    sage = forms.IntegerField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    # gender = forms.ChoiceField(choices=g)
    gender = forms.ChoiceField(choices=g, widget=forms.RadioSelect)
    saddress = forms.CharField(widget=forms.Textarea(attrs={'cols':25,'rows':5}))
    cource = forms.MultipleChoiceField(choices=c, widget=forms.CheckboxSelectMultiple)
    