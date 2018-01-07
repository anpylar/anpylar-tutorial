###############################################################################
# Copyright 2018 The AnPyLar Team. All Rights Reserved.
# Use of this source code is governed by an MIT-style license that
# can be found in the LICENSE file at http://anpylar.com/mit-license
###############################################################################
from browser import window
from anpylar import Observable


class DialogService:

    def confirm(self, message='Is it OK?'):
        confirmation = window.confirm(message)
        return Observable.of(confirmation)
