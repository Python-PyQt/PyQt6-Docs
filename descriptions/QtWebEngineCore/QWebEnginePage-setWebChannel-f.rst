.. sip:method-description::
    :status: todo
    :pysig: aba1fe5b9eb8959d990ef7561b35188c
    :realsig: (QWebChannel*,quint32)
    :digest: 047ef9c83a7e7bbd48afc102c6a8802b

Sets the web channel instance to be used by this page to *channel* and connects it to web engine's transport using Chromium IPC messages. The transport is exposed in the JavaScript world *worldId* as ``qt.webChannelTransport``, which should be used when using the `Qt WebChannel JavaScript API <https://doc.qt.io/qt-6/qtwebchannel-javascript.html>`_.

**Note:** The page does not take ownership of the channel object.

**Note:** Only one web channel can be installed per page, setting one even in another JavaScript world uninstalls any already installed web channel.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.webChannel`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.ScriptWorldId`.
