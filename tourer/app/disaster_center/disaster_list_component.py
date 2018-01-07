###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html
from .disaster_service import Disaster


class DisasterListComponent(Component):
    htmlsheet = '''
    <ul class="items"></ul>
    <router-outlet></router-outlet>
    '''

    bindings = {
        'selected': Disaster(),
        'disasters': [],
    }

    def __init__(self):
        self.disaster_service.get_disasters().subscribe(self.disasters_)

    def li_disasters(self, disasters):
        for disaster in disasters:
            with html.li() as li:
                li._class.selected(self.selected_.did_ == disaster.did)

                with html.a(routerlink=('', {'did': disaster.did})):
                    html.span(disaster.did, Class='badge')
                    html.txt()._fmt(disaster.name_)

            li._bindx.click(lambda d=disaster: self.selected_(d))

    def render(self, node):
        with node.select('ul') as ul:
            ul._render(self.li_disasters, self.disasters_)
