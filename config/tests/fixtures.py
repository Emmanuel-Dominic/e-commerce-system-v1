import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
