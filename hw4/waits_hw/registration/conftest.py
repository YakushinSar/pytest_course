import pytest
from faker import Faker


@pytest.fixture
def random_login():
    fake = Faker()
    return fake.user_name()


@pytest.fixture
def random_password():
    fake = Faker()
    return fake.password()
