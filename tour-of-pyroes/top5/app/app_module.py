###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module

from .app_component import AppComponent
from .app_routing import AppRouting
from .pyro_service import PyroService


class AppModule(Module):

    components = AppComponent

    bindings = {}

    services = {
        'pyro_service': PyroService,
    }

    routes = AppRouting

    def __init__(self):
        pass
