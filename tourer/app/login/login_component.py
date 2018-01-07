###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from anpylar import Component


class LoginComponent(Component):
    htmlsheet = '''
    <h2>LOGIN</h2>
    <p [msg_]>{}</p>
    <p>
      <button
        *_display="auth_service.is_logged_ == 0"
        (click)=login>Login
      </button>
      <button
        *_display="auth_service.is_logged_"
        (click)=logout>Logout
      </button>
    </p>
    '''

    bindings = {
        'msg': '',
    }

    def loading(self):
        self.set_message()

    def set_message(self):
        self.msg = 'Logged ' + ('in' if self.auth_service.is_logged else 'out')

    def login(self):
        def to_login(x):
            self.set_message()
            if self.auth_service.is_logged:
                sid = self.params.get('session_id', 0)
                self.router.route_to(self.auth_service.redir_path,
                                     session_id=sid)
                self.auth_service.redir_path = ''

        self.auth_service.login().subscribe(to_login)

    def logout(self):
        self.auth_service.logout()
        self.set_message()
