#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
from anpylar import Component, html


class DashboardComponent(Component):

    def loading(self):
        self.pyro_service.get_pyroes().subscribe(self.pyroes_)

    def unloading(self):
        self.pyroes_ = []

    def render(self, node):
        with node.select('div') as d:
            d._render(self.render_top_pyroes, self.pyroes_)

    def render_top_pyroes(self, pyroes):
        for p in pyroes[:4]:
            with html.a(Class='col-1-4',
                        routerlink=('/detail', {'pyd': p.pyd})):

                with html.div(Class='module pyro'):
                    html.h4('{name}')._fmt(name=p.name_)
