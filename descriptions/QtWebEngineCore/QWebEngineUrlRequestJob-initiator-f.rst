.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: () const
    :digest: 6678678b91acad9b96dc1b1cc1121b9b

Returns the serialized origin of the content that initiated the request.

Generally, the origin consists of a scheme, hostname, and port. For example, ``"http://localhost:8080"`` would be a valid origin. The port is omitted if it is the scheme's default port (80 for ``http``, 443 for ``https``). The hostname is omitted for non-network schemes such as ``file`` and ``qrc``.

However, there is also the special value ``"null"`` representing a unique origin. It is, for example, the origin of a sandboxed iframe. The purpose of this special origin is to be always different from all other origins in the same-origin check. In other words, content with a unique origin should never have privileged access to any other content.

Finally, if the request was not initiated by web content, the function will return an empty :sip:ref:`~PyQt6.QtCore.QUrl`. This happens, for example, when you call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.setUrl`.

This value can be used for implementing secure cross-origin checks.
