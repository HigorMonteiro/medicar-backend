from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_date(day):
    if day < date.today():
        day = day.strftime('%d/%m/%Y')
        raise ValidationError(
            _('%(day)s is less than the current date'),
            params={'day': day},
        )
