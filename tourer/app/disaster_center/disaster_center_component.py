###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class DisasterCenterComponent(Component):
    htmlsheet = '''
    <h2>Disaster Center</h2>
    <router-outlet></router-outlet>
    '''
