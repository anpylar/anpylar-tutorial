###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html
from .pyroes import PyroesComponent
from .pyro_detail import PyroDetailComponent


class AppComponent(Component):

    title = 'Tour of Pyroes'

    bindings = {}

    def render(self, node):
        PyroesComponent()
