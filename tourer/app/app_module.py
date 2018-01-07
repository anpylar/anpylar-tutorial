###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module

from .app_component import AppComponent
from .compose_message import ComposeMessageComponent
from .page_not_found_component import PageNotFoundComponent

from .admin import AdminModule
from .disaster_center import DisasterCenterModule
from .pyroes import PyroesModule
from .login import LoginModule

from .auth_service import AuthService
from .dialog_service import DialogService


class AppModule(Module):

    modules = LoginModule, PyroesModule

    components = AppComponent

    bindings = {}

    services = {
        'auth_service': AuthService,
        'dialog_service': DialogService,
    }

    routes = [
        {'path': 'compose', 'component': ComposeMessageComponent,
         'outlet': 'popup'},

        {'path': 'disaster-center', 'load_children': [DisasterCenterModule]},

        {'path': 'admin', 'load_children': [AdminModule]},

        {'path': '', 'redirect_to': '/superpyroes', 'path_match': 'full'},

        {'path': '*', 'component': PageNotFoundComponent},
    ]
