# -*- coding: utf-8 -*-

from model.group import Group


def test_delete_first_group(app):

    app.group.open_groups_page()
    if not app.group.count():
        app.group.create(Group(name="Create group"))
        app.group.return_to_groups_page()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    app.group.return_home_page()

