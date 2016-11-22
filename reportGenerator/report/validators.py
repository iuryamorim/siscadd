from django.core.exceptions import ValidationError


def validate_formato(value):
    formato = str(value)[-3::]
    if formato != "csv":
        raise ValidationError('Formato Inválido!')