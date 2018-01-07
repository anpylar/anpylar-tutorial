###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module

from .app_component import AppComponent


class AppModule(Module):

    components = AppComponent

    bindings = {}

    services = {}

    routes = []

    def __init__(self):
        pass
