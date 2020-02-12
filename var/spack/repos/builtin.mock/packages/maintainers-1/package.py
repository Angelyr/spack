# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Maintainers1(Package):
    """Package with a maintainers field."""

    homepage = "http://www.example.com"
    url      = "http://www.example.com/maintainers-1.0.tar.gz"

    maintainers = ['user1', 'user2']

    version('1.0', '0123456789abcdef0123456789abcdef')

    def install(self, spec, prefix):
        pass
