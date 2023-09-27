import importlib
import pytest
import os.path
from fixture.application import Application
from comtypes.client import CreateObject
from model.group import Group


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("c:\\temp\\AddressBook\\Addressbook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_xlsx(file):
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % file)
    xl = CreateObject("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    wb = xl.Workbooks.Open(file_name)
    row = 1
    groups_list = []
    while True:
        group_name = xl.Cells[row, 1].Value[()]
        if isinstance(group_name, str):
            groups_list.append(Group(group_name))
            row = row + 1
        else:
            break

    wb.Close(0)
    xl.Quit()

    return groups_list
