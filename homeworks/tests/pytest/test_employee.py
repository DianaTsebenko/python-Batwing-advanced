from employee import Employee

employer = Employee("diana", "tsebenko", 400)


def test_email():
    assert employer.email == "diana.tsebenko@email.com"


def test_fullname():
    assert employer.fullname != "alex white"
    assert employer.fullname == "diana tsebenko"


def test_apply_raise():
    employer.apply_raise()
    assert employer.pay == 420


