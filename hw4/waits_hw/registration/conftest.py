import pytest
from faker import Faker




def random_login():
    fake = Faker()
    return fake.user_name()
    print(fake)


@pytest.fixture
def random_password():
    fake = Faker()
    return fake.password()
