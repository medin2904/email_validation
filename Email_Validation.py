#!python3

# checks there are any invalid characters in email prefix and domain
def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."

    for character in string:
        if character not in valid:
            return True
    return False


def is_valid(email):
    # checks for @ symbol, if it's more or less than one "@", returns invalid
    at = email.count("@")
    for char in email:
        if at != 1:
            return False

    # splits email with prefix (before @) and domain (after @)
    prefix, domain = email.split("@")

    # if no prefix, returns invalid
    if len(prefix) == 0:
        return False

    dot = email.count(".")
    for char in email:
        if dot != 1:
            return False

    # splits domain name and extension if "." exists
    if "." in domain:
        domain_name, extension = domain.split(".")
        if len(domain_name) == 0:
            return False
        if len(extension) == 0:
            return False

    # invalidates email without "." in domain
    if "." not in domain:
        return False

    if has_invalid_characters(prefix):
        return False
    if has_invalid_characters(domain):
        return False

    return True


emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com",
]
for email in emails:
    if is_valid(email) == True:
        print(email + " is valid")
    if is_valid(email) == False:
        print(email + " is invalid")