import pytest
import subprocess

from constants import SERVER, DATABASE
# from src.book_drop.sql_address_repository import SqlAddressRepository
# from src.person.sql_person_repository import SqlPersonRepository
#

@pytest.fixture(scope="session", autouse=True)
def setup():
    reset_test_database()


def reset_test_database():
    print("\n\nReloading database....")

    process = subprocess.Popen(["powershell", "..\\RebuildDatabase-local.ps1",
                                "-Server", '"(local)\\SQLEXPRESS"',
                                "-Database", '"cc520"',
                                '-Dir', '..\\src'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True, shell=True)

    for result in process.communicate():
        print(result)

    process.communicate()

    print("done.\n\n")


# @pytest.fixture(scope="function")
# def address_repo():
#     yield SqlAddressRepository(server=SERVER, database=DATABASE)
#     reset_test_database()
#
#
# @pytest.fixture(scope="function")
# def person_repo():
#     yield SqlPersonRepository(server=SERVER, database=DATABASE)
#     reset_test_database()
