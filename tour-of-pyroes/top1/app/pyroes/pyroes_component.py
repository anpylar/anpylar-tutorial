###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html
from app.pyro import Pyro


class PyroesComponent(Component):

    bindings = {
        'pyro': Pyro(pyd=11, name='Pyro Nakamura')
    }

    def render(self, node):
        pass
