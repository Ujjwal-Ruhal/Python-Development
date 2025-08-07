def is_valid_email(email):
    # Check if there is exactly one '@'
    if email.count('@') != 1:
        return "Invalid EmailId"

    # Split into local and domain parts
    local, domain = email.split('@')

    # Check if local part is not empty
    if not local:
        return "Invalid EmailId"

    # Check if domain part has at least one dot
    if '.' not in domain:
        return "Invalid EmailId"

    # Domain should not strt or end with a dot
    if domain.startswith('.') or domain.endswith('.'):
        return "Invalid EmailId"

    # No spaces allowed
    if ' ' in email:
        return "Invalid EmailId"

    return "Valid EmailId"

emails = [
    "test@example.com",
    "Ujjwalruhal@gmail.com",
    "Udit001@gmail.com",
    "user@.com",
    "noatsymbol.com",
    "user@domain.co.in"
]

for e in emails:
    print(f"{e} -> {is_valid_email(e)}")
