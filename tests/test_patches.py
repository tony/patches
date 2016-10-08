# -*- coding: utf-8 -*-
from patches import Entry


def test_has_raw_data():
    assert Entry.raw_data is None
