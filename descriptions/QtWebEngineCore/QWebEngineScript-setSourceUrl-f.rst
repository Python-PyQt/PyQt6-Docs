.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: aa06340b866f6bd627298a133d9e22d9

Sets the remote source location of the user script to *url*.

Unlike :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.setSourceCode`, this function allows referring to user scripts that are not already loaded in memory, for instance, when stored on disk.

Setting this value will change the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.sourceCode` of the script.

**Note:** At present, only file-based sources are supported.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.sourceUrl`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.setSourceCode`.
