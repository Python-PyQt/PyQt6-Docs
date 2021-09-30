.. sip:method-description::
    :status: todo
    :pysig: c714d0f3ca5fedc4bf1c1f876e912816
    :realsig: () const
    :digest: 3c208729b07f4d4ab5be78375c389078

Returns a pointer to the web channel instance used by this page or a null pointer if none was set. This channel automatically uses the internal web engine transport mechanism over Chromium IPC that is exposed in the JavaScript context of this page as ``qt.webChannelTransport``.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setWebChannel`.
