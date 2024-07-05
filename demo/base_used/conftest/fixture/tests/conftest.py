import pytest


@pytest.fixture(scope="package")
def package_scope_fixture():
    print("\nSetup for package scope")
    yield "package scope fixture"
    print("\nTeardown for package scope")
