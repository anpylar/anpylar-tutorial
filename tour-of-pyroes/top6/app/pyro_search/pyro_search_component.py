###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component, html


class PyroSearchComponent(Component):
    selector = 'pyro-search'

    bindings = {
        'pyroes': [],
        'searchterm': '',
    }

    services = {}

    def __init__(self):
        # connect searchterm to the found pyroes to be displayed
        self.searchterm_ \
            .debounce(300) \
            .distinct_until_changed() \
            .switch_map(lambda x: self.pyro_search.search(x) if x else []) \
            .catch_exception(lambda e: print('search error:', e) or []) \
            .subscribe(self.pyroes_)

    def unloading(self):
        self.pyroes = []  # clear result
        self.searchterm = ''  # clear search box

    def render(self, node):

        def sought_pyroes(pyroes):
            for p in pyroes:
                with html.li() as li:  # per-pyro list item
                    # per-pyro anchor routing path with parameter pyd
                    html.a(p.name, routerlink=('/detail', {'pyd': p.pyd}))

        with node.select('ul') as ul:
            ul._render(sought_pyroes, self.pyroes_)
