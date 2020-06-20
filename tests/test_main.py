from leap_year.main import MyYear


def test_save_year():
    assert MyYear(1000).year == 1000


def test_to_string():
    assert str(MyYear(1000)) == "1000"


def test_is_leap_year_of_multiple_of_4():
    target_class = MyYear(2020)
    assert target_class.is_leap()


def test_is_not_leap_integer_multiple_of_4():
    target_class = MyYear(2021)
    assert not target_class.is_leap()
