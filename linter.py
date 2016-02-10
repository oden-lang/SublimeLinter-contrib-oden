#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Albin Theander
# Copyright (c) 2016 Albin Theander
#
# License: MIT
#

"""This module exports the Oden plugin class."""

from SublimeLinter.lint import Linter, util


class Oden(Linter):
    """Provides an interface to oden."""

    syntax = ('Oden', 'oden')
    cmd = ('oden', 'lint')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0'
    regex = r'[^:]*:(?P<line>\d+):(?P<col>\d+):\s*(?P<error>error:)?\s+(?P<message>.*)'
    tempfile_suffix = 'oden'
    error_stream = util.STREAM_BOTH
