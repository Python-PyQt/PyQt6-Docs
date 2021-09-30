.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: e553a592bfa844602c54e9dbfc13333a

Returns the user-agent string sent with HTTP to identify the browser.

**Note:** On Windows 8.1 and newer, the default user agent will always report "Windows NT 6.2" (Windows 8), unless the application does contain a manifest that declares newer Windows versions as supported.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.setHttpUserAgent`.
