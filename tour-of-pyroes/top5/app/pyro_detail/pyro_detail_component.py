###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html

from app.pyro import Pyro


class PyroDetailComponent(Component):
    bindings = {
        'pyro': Pyro(),
    }

    def loading(self):
        self.pyro_service \
            .get_pyro(self.params.get('pyd', 0)) \
            .subscribe(self.pyro_)  # fetch async and fire self.pyro_ when done

    def unloading(self):
        self.pyro = Pyro()  # clear the editor on unloading: set null Pyro

    def render(self, node):
        pass  # the entire work is done in the html rendering
