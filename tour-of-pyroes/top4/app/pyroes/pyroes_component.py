###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html
from app.pyro import Pyro


class PyroesComponent(Component):

    bindings = {
        'selected': Pyro(),
        'pyroes': [],  # observable for receiving pyroes
    }

    def __init__(self):
        # get the pyroes from service into the observable
        self.pyro_service.get_pyroes().subscribe(self.pyroes_)

    def render(self, node):
        with node.select('ul') as ul:  # find node where to display the list
            # Render under "ul" using
            #   callback: render_pyroes
            #   when: the observable self.pyroes_ is signaled
            ul._render(self.render_pyroes, self.pyroes_)

    def render_pyroes(self, pyroes):
        # Because this was registered with ul._render, any rendering action
        # takes place under ul, which is empty when entering here
        for pyro in pyroes:
            with html.li() as li:  # create a list item per Pyro
                # if the selected pyro is this pyro ... set a class attr
                li._class.selected(self.selected_.pyd_ == pyro.pyd)
                # bind a click to do self.selected_(pyro)
                li._bindx.click(self.selected_, pyro)
                # show the pyd in a <apan> as a badge (child of list item)
                html.span(pyro.pyd, Class='badge')
                # show the name as text inside the list item
                html.txt(' {name}')._fmt(name=pyro.name_)
