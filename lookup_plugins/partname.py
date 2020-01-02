# (c) 2019, Uli Martens <uli@youam.net>
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import re
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.utils.listify import listify_lookup_plugin_terms

class LookupModule(LookupBase):

    def usage(self, msg):
         raise AnsibleError(
                 "partname( blockdev, partno ): %s" % msg )

    def run(self, terms, variables, **kwargs):
        if not len(terms) == 2:
            self.usage( "need two args" )

        blockdev = terms[0]
        partno   = terms[1]

        if re.search(r'\d+$', blockdev) is None:
            ret = "%s%s"  % (blockdev, partno)
        else:
            ret = "%sp%s" % (blockdev, partno)

        return [ ret ]
