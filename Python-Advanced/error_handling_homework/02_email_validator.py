from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustNotContainInvalidCharacters(Exception):
    pass


MIN_USERNAME_LENGTH = 5
VALID_DOMAINS = ('com', 'bg', 'org', 'net')
valid_email_pattern = r'\w+'

email = input()

while email != 'End':

    if len(email.split('@')[0]) < MIN_USERNAME_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')
    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following:{", ".join("." + domain for domain in VALID_DOMAINS)}')
    elif len(findall(valid_email_pattern, email.split('@')[0])) > 1:
        raise MustNotContainInvalidCharacters('Some of the used characters are not allowed')

    print("Email is valid")

    email = input()