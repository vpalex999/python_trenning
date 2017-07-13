# -*- coding: utf-8 -*-

from timeit import timeit
from model.group import Group


def test_group_list(app, db):

    print(timeit(lambda: app.group.get_group_list(), number=1))
    # ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda : db.get_group_list(), number=1000))
    # db_list = map(clean, db.get_group_list())
    assert False # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)