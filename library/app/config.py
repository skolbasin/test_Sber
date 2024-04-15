from django.core.exceptions import ValidationError


def validate_username(value):
    """
    Валидация в которой поле должно состоять из двух слов, каждое слово должно начинаться с заглавной буквы.
    :param value:
    :return: ValidationError
    """
    words = value.split()
    if len(words) != 2 or not all(word.istitle() for word in words):
        raise ValidationError(
            'Необходимо указать 2 слова, каждое слово должно начинаться с заглавной буквы.'
        )


def validate_age(value):
    """
    Валидация на возраст
    :param value:
    :return: ValidationError
    """
    if value < 18 or value > 130:
        raise ValidationError(
            'Возраст должен быть от 18 до 130 лет'

        )
