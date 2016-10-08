# -*- coding: utf-8 -*-
# flake8: NOQA
"""Portfolio management for open source contributors.

patches
~~~~~~~

:copyright: Copyright 2016 Tony Narlock.
:license: BSD, see LICENSE for details

"""

class Source(object):

    def get_results(self):
        pass



class Entry(object):

    raw_data = None


class Patch(object):

    def __str__(self):
        return self._raw_data


class Communique(object):

    def __str__(self):

        return self._raw_data
