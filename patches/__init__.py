# -*- coding: utf-8 -*-
# flake8: NOQA
"""Portfolio management for open source contributors.

patches
~~~~~~~

:copyright: Copyright 2016 Tony Narlock.
:license: BSD, see LICENSE for details

"""

from typing import List


class Result(object):

    pass


class Source(object):

    def get_results(self) -> List[Result]:
        pass


class Entry(object):

    raw_data = None  # type: str


class Patch(Entry):

    def __str__(self) -> str:
        return self.raw_data


class Communique(Entry):

    def __str__(self) -> str:
        return self.raw_data
