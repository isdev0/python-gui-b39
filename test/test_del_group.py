import random
from model.group import Group


def test_delete_random_group(app):
    if len(app.group.get_all()) == 1:
        app.group.create(Group("TestGroupName" + str(random.randrange(99))))

    old_groups = app.group.get_all()
    group = random.choice(old_groups)

    print("\nRandom group: " + group.name)
    app.group.delete_by_name(group.name)

    new_groups = app.group.get_all()
    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(group)
    assert old_groups == new_groups
