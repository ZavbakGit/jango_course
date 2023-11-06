from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
        'min_length': 'Короткое имя',
        'max_length': 'Длинное имя',
        'required': 'Пустое имя'
    })

    rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1, )
    # surname = forms.CharField()
    # feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
