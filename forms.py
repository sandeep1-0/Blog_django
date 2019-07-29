from django import forms

class User_reg(forms.Form):


    username=forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username'
        })
    )
    firstname=forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'First Name'
        })
    )
    lastname=forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'Last Name'
        })
    )
    password=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'required min 8'
        })
    )
    cn=(
        ('m', 'male'),
        ('f', 'female')
    )
    gender=forms.ChoiceField(choices=cn, widget=forms.RadioSelect)

    email_id = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder':'Email'
        })
    )

    address=forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':'Enter how to reach you'
        })
    )


