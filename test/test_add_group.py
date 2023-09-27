from random import randrange
from model.group import Group


def _test_simple_add_group(app):
    group_name = "TestGroupName" + str(randrange(99))
    old_groups = app.group.get_all()
    app.group.create(Group(group_name))
    new_groups = app.group.get_all()
    old_groups.append(Group(group_name))
    assert sorted(old_groups, key=Group.name) == sorted(new_groups, key=Group.name)


def test_add_group(app, xlsx_groups):
    old_groups = app.group.get_all()
    app.group.create(xlsx_groups)
    new_groups = app.group.get_all()
    old_groups.append(xlsx_groups)
    assert sorted(old_groups, key=Group.name) == sorted(new_groups, key=Group.name)

