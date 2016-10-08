|pypi| |docs| |build-status| |coverage| |license|

Its time to address the perenniel issue open source developers face.

What we need is a way to grab patches (diffs), the project, the issue
tracker URL, any tags we want to specify for it, and then finally, a way
to output it to different front ends (XML, JSON, HTML) so on.

How will it work
================

- github API

  pros: quicker than download full git / hg repositories

  cons: only contributions made through pull requests are gathered.

- version control

  pros: most thorough

  cons: requires (in the case of git, mercurial) downloading whole
  repositories, then searching them.

- trackers

  examples: bugzilla, github, gitlab

  pros: can grab direct patches from version control where authors aren't
  as easy to pluck out.


What users need to add
======================

Most VCS / tracking systems use VCS. For using Github API, you need to use
an API token.


.. |pypi| image:: https://img.shields.io/pypi/v/patches.svg
    :alt: Python Package
    :target: http://badge.fury.io/py/patches

.. |build-status| image:: https://img.shields.io/travis/tony/patches.svg
   :alt: Build Status
   :target: https://travis-ci.org/tony/patches

.. |coverage| image:: https://codecov.io/gh/tony/patches/branch/master/graph/badge.svg
    :alt: Code Coverage
    :target: https://codecov.io/gh/tony/patches
    
.. |license| image:: https://img.shields.io/github/license/tony/patches.svg
    :alt: License 

.. |docs| image:: https://readthedocs.org/projects/patches/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://readthedocs.org/projects/patches/
