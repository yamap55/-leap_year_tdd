from leap_year.main import MyYear


def test_save_year():
    assert MyYear(1000).year == 1000


def test_to_string():
    assert str(MyYear(1000)) == "1000"
