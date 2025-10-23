.. sip:method-description::
    :status: todo
    :pysig: 30abb1de6f61e3fb45b37bea7fd11ba3
    :realsig: (const QList<QSslError>&)
    :digest: abb54e635c7516a95db13b4d643d328a

This method tells :sip:ref:`~PyQt6.QtNetwork.QSslSocket` to ignore only the errors given in *errors*.

**Note:** Because most SSL errors are associated with a certificate, for most of them you must set the expected certificate this SSL error is related to. If, for instance, you want to connect to a server that uses a self-signed certificate, consider the following snippet:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslsocket.py
    :lines: 112-119

Multiple calls to this function will replace the list of errors that were passed in previous calls. You can clear the list of errors you want to ignore by calling this function with an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslHandshakeErrors`.
