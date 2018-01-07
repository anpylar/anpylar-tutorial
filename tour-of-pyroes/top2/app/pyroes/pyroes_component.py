###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html
from app.pyro import Pyro
from app.mock_pyroes import Pyroes


class PyroesComponent(Component):

    bindings = {
        'selected': Pyro(),
    }

    def render(self, node):
        with node.select('ul'):  # find the node where to display the list
            for pyro in Pyroes:
                with html.li() as li:  # create a list item per Pyro
                    # if the selected pyro is this pyro ... set a class attr
                    li._class.selected(self.selected_.pyd_ == pyro.pyd)
                    # bind a click to do self.selected_(pyro)
                    li._bindx.click(self.selected_, pyro)
                    # show the pyd in a <apan> as a badge (child of list item)
                    html.span(pyro.pyd, Class='badge')
                    # show the name as text inside the list item
                    html.txt(' {name}')._fmt(name=pyro.name_)
