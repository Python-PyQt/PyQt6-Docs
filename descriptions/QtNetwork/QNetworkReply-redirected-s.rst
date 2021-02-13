.. sip:signal-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 3a4f3d62a896afa7367cabf401564b49

This signal is emitted if the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.ManualRedirectPolicy` was set in the request and the server responded with a 3xx status (specifically 301, 302, 303, 305, 307 or 308 status code) with a valid url in the location header, indicating a HTTP redirect. The *url* parameter contains the new redirect url as returned by the server in the location header.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy`.
