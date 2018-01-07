###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html


class PyroesComponent(Component):

    def render(self, node):
        # render under ul in render_pyroes when observable self.pyroes_ fires
        with node.select('ul') as ul:  # find node where to display the list
            ul._render(self.render_pyroes, self.pyroes_)

    def render_pyroes(self, pyroes):
        for pyro in pyroes:
            with html.li() as li:  # per-pyro list item
                # per-pyro anchor routing path with parameter pyd
                with html.a(routerlink=('/detail', {'pyd': pyro.pyd})):
                    html.span(pyro.pyd, Class='badge')  # show pyd as badge
                    html.txt(' {name}')._fmt(name=pyro.name_)  # obs name_
