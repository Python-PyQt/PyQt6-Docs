.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: fa8e34b8b49283fc0ad4f11254f50c91

Returns the user-agent string sent with HTTP to identify the browser.

**Note:** On Windows 8.1 and newer, the default user agent will always report "Windows NT 6.2" (Windows 8), unless the application does contain a manifest that declares newer Windows versions as supported.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpUserAgent`, `Windows Application Manifest <https://doc.qt.io/qt-6/qtwebengine-platform-notes.html#windows-manifest>`_.
