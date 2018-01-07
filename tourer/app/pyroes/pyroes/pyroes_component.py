###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html


class PyroesComponent(Component):
    htmlsheet = '''
    <h2>Pyroes</h2>
    <ul class="items"></ul>
    <button routerLink="/save-the-world">Save the World</button>
    '''

    stylepath = None

    bindings = {
        'pyd': 0,
        'pyroes': [],
    }

    def loading(self):
        self.pyro_service.get_pyroes() \
            .subscribe(self.pyroes_)

    def unloading(self):
        self.pyroes = []

    def li_pyroes(self, pyroes):
        for pyro in pyroes:
            with html.li() as li:
                # li._class.selected(self.selected_.pyd_ == pyro.pyd)
                li._class.selected(self.pyd == pyro.pyd)
                li._bindx.click(self.pyd_, pyro)
                with html.a(routerlink=('/pyro', {'pyd': pyro.pyd})):
                    html.span(pyro.pyd, Class='badge')
                    html.txt(' {name}')._fmt(name=pyro.name_)

    def render(self, node):
        with node.select('ul') as ul:
            ul._render(self.li_pyroes, self.pyroes_)
