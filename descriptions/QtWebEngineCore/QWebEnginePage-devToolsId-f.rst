.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: f0d4be0f72adc272a2772c6e87a4dca6

Returns the id of the developer tools host associated with this page.

If remote debugging is enabled (see `Qt WebEngine Developer Tools <https://doc.qt.io/qt-6/qtwebengine-debugging.html#qt-webengine-developer-tools>`_), the id can be used to build the URL to connect to the developer tool websocket: ``ws://localhost:<debugging-port>/devtools/page/<id>)``. The websocket can be used to to interact with the page using the `DevTools Protocol <https://chromedevtools.github.io/devtools-protocol/>`_.
