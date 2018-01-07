###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Module

from .disaster_center_component import DisasterCenterComponent
from .disaster_list_component import DisasterListComponent
from .disaster_detail_component import DisasterDetailComponent
from .disaster_center_home_component import DisasterCenterHomeComponent

from .disaster_service import DisasterService


class DisasterCenterModule(Module):

    services = {
        'disaster_service': DisasterService,
    }

    routes = [{
        'path': '',
        'component': DisasterCenterComponent,
        'children': [
            {
                'path': '',
                'component': DisasterListComponent,
                'children': [
                    {
                        'path': '',
                        'component': DisasterDetailComponent,
                        'params': {'did': int},  # transformation function
                    },
                    {
                        'path': '',
                        'component': DisasterCenterHomeComponent,
                    }
                ]
            }
        ]
    }]
