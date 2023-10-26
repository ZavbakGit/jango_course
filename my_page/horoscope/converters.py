from datetime import datetime


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class MYFloatConverter:
    regex = '[+-]?[0-9]+\.[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class MYDateConverter:
    regex = '[0-9]{2}.[0-9]{2}.[0-9]{4}'

    def to_python(self, value):
        return datetime.strptime(value, '%d.%m.%Y')

    def to_url(self, value):
        return value.strftime('%d.%m.%Y')
