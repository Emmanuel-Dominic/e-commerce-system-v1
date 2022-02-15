import pytest
from ecommerce.inventory import models


# Create your tests here.
@pytest.mark.dbfixture
@pytest.mark.parametrize("id, name, slug, is_active", [
    (3, "fashion", "fashion", True),
    (4, "trainers", "trainers", True),
    (5, "baseball", "baseball", True)
    ]
)
def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active

@pytest.mark.parametrize("name, slug, is_active", [
    ("fashion", "fashion", 1),
    ("trainers", "trainers", 1),
    ("baseball", "baseball", 1)
    ]
)
def test_inventory_category_dbfixture(db, category_factory, name, slug, is_active):
    result = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active
