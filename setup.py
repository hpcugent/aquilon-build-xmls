#!/usr/bin/env python
# -*- coding: latin-1 -*-
#
# Copyright 2009-2013 Ghent University
# Copyright 2009-2013 Luis Fernando Muñoz Mejías
#
#
"""Basic setup.py for packaging the Aquilon build scripts"""

import sys
import os
from distutils.core import setup
import glob

def get_data_files():

    l = []
    for d, v, f in os.walk("build-xmls"):
        print d, v, f
        if f:
            l.append(("/usr/share/aquilon/%s" % d,
                      [os.path.join(d, x) for x in f]))
    return l

setup(name="aquilon-build-xml",
      version="1.0.0",
      description="Custom build.xml files for using different versions of the Pan compiler",
      long_description="""The build.xml shipped with the Aquilon RPM is specific to Morgan Stanley.

We ship here build.xml files used at UGent with different versions of the Pan compiler""",
      license="Apache 2",
      author="HPC UGent",
      author_email="hpc-admin@lists.ugent.be",
      data_files=get_data_files(),
      url="http://quattor.org")
