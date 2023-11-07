from django import forms
from .models import Feedback


# class FeedBackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'min_length': 'Короткое имя',
#         'max_length': 'Длинное имя',
#         'required': 'Пустое имя'
#     })
#     surname = forms.CharField()
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1, )
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'rating', 'feedback']
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'rating': 'Рейтинг',
            'feedback': 'Отзыв',
        }

        error_messages = {
            'name': {'max_length': 'ой как много символов',
                     'min_length': 'ой как мало символов',
                     'required': 'Не должно быть пустым'
                     },
            'surname': {'max_length': 'ой как много символов',
                        'min_length': 'ой как мало символов',
                        'required': 'Не должно быть пустым'
                        },
            'feedback': {'max_length': 'ой как много символов',
                         'min_length': 'ой как мало символов',
                         'required': 'Не должно быть пустым'
                         }
        }
