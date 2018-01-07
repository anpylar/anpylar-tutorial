###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html


class PyroesComponent(Component):

    bindings = {
        'pyro_name': '',
    }

    def loading(self):
        self.pyro_service.get_pyroes().subscribe(self.pyroes_)

    def unloading(self):
        self.pyroes_ = []

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

                with html.button('x', Class='delete') as b:
                    # def param avoids closure using last pyro.pyd
                    def pyro_delete(evt, pyd=pyro.pyd):
                        evt.stopPropagation()  # avoid evt clicking on "a"
                        self.pyro_delete(pyd)

                    b._bind.click(pyro_delete)  # use "bind" to get event

    def pyro_add(self):
        self.pyro_service.add_pyro(self.pyro_name).subscribe(
            lambda pyro: self.pyroes_(self.pyroes + [pyro])
        )

        self.pyro_name_ = ''

    def pyro_delete(self, pyd):
        self.pyro_service.delete_pyro(pyd) \
            .subscribe(
                lambda x: self.pyroes_([x for x in self.pyroes if x.pyd != pyd])
            )
