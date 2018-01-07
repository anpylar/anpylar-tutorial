###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html


class AppComponent(Component):

    title = 'Tour of Pyroes'

    bindings = {
        'pyroes': [],
    }

    def __init__(self):
        self.pyro_service.get_pyroes().subscribe(self.pyroes_)
