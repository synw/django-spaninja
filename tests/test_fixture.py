def test_users_fixtures(visitor, staff, administrator):
    assert staff
    assert administrator
    assert visitor
    assert visitor.is_staff is False
    assert staff.is_staff is True
    assert staff.is_superuser is False
    assert administrator.is_superuser is True
    assert administrator.is_staff is True
    assert visitor is not staff
    assert visitor is not administrator
