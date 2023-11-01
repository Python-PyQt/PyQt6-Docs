.. sip:method-description::
    :status: todo
    :pysig: 0d9647126e382a599df85003d20a23f2
    :realsig: (const QString&, quint16)
    :digest: a5046764598424cf15be78aa3c425ab0

Initiates a connection to the host given by *hostName* at port *port*. This function is useful to complete the TCP handshake to a host before the HTTP request is made, resulting in a lower network latency.

**Note:** This function has no possibility to report errors.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.connectToHostEncrypted`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`.
