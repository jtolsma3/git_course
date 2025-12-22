import datetime

def get_birthdate(person = "me"):
    if person.lower().strip() == "me":
        return datetime.datetime(year = 1986, month = 7, day = 19)
    if person.lower().strip() == "mom":
        return datetime.datetime(year = 1953,month = 5, day = 29)
    if person.lower().strip() == "dad":
        return datetime.datetime(year = 1950,month = 3, day = 5)
    else:
        raise ValueError("valid values for 'person' are 'me', 'mom', and 'dad' only")