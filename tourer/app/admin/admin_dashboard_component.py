###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class AdminDashboardComponent(Component):
    htmlsheet = '''
    <p>Dashboard</p>
    Session Id:<txt [session_id_]>{}</txt>
    '''

    bindings = {
        'session_id': ''
    }

    def loading(self):
        self.session_id = self.params.get('session_id', '')
