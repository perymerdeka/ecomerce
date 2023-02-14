import pytest


pytestmark = pytest.mark.django_db

class TestCategoryModel():
    def test_str_method(self, category_factory):
        x = category_factory(name="test_cat")

        assert x.__str__() == "test_cat"


class TestBrandModel():
    pass

class TestProductModel():
    pass