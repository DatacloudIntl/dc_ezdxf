#!/usr/bin/env python
#coding:utf-8
# Author:  mozman -- <mozman@gmx.at>
# Purpose: test sections
# Created: 12.03.2011
# Copyright (C) 2011, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals

import unittest

from ezdxf.lldxf.tagger import internal_tag_compiler
from ezdxf.tools.test import DrawingProxy
from ezdxf.sections.sections import Sections
from ezdxf.lldxf.const import DXFStructureError


class TestSections(unittest.TestCase):
    def setUp(self):
        self.dwg = DrawingProxy('AC1009')
        self.sections = Sections(internal_tag_compiler(TEST_HEADER), self.dwg)

    def test_constructor(self):
        header = self.sections.header
        self.assertIsNotNone(header)

    def test_getattr(self):
        result = self.sections.header
        self.assertIsNotNone(result)

    def test_error_getitem(self):
        with self.assertRaises(DXFStructureError):
            self.sections.test

    def test_error_getattr(self):
        with self.assertRaises(DXFStructureError):
            self.sections.test


TEST_HEADER = """  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1018
  9
$DWGCODEPAGE
  3
ANSI_1252
  0
ENDSEC
  0
SECTION
  2
TABLES
  0
ENDSEC
  0
SECTION
  2
ENTITIES
  0
ENDSEC
  0
EOF
"""

if __name__ == '__main__':
    unittest.main()