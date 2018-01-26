Uploading the tutorial samples to plunker
=========================================

Bulk Upload is achieved using the ``plunk`` tool. Available at:

  - https://www.npmjs.com/package/plunk

Before running it

  - Log into *plunker*
  - Execute the following code in the console::

      document.cookie.match(/plnk_session=(\w+)/)[1]

This will produce an identifier which can be provided as the parameter to
``--auth.id`` below.

If plunk is installed locally, a sample execution can be::

  ./node_modules/.bin/plunk \
      --auth.id {THE_AUTH_ID_FROM_PLUNKER} \
      --dir {DIRECTORY TO UPLOAD}

If successful, the answer will look like::

  http://plnkr.co/edit/{plunker_identifier}?p=preview

The samples contain already the right metadata for the upload
