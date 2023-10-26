from django.test import TestCase
from .views import signs_dictionary


# Create your tests here.

# python manage.py test horoscope
class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEquals(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEquals(response.status_code, 200)
        self.assertIn("Весы - седьмой знак зодиака, планета Венера", response.content.decode())

    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, "/horoscope/libra/")

    def test_signs(self):
        i = 1
        for sign, dates in signs_dictionary.items():
            response = self.client.get(f'/horoscope/{sign}/')
            print(f'{sign} : {dates}')
            self.assertEquals(response.status_code, 200)
            self.assertIn(dates, response.content.decode())

            response = self.client.get(f'/horoscope/{i}/')
            self.assertEquals(response.status_code, 302)
            self.assertEquals(response.url, f"/horoscope/{sign}/")
            i += 1
