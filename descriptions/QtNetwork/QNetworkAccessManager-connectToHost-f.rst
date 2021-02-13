.. sip:method-description::
    :status: todo
    :pysig: e395100a0b520362adb0414a73494b2f
    :realsig: (const QString&,quint16)
    :digest: a5046764598424cf15be78aa3c425ab0

Initiates a connection to the host given by *hostName* at port *port*. This function is useful to complete the TCP handshake to a host before the HTTP request is made, resulting in a lower network latency.

**Note:** This function has no possibility to report errors.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.connectToHostEncrypted`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.get`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.deleteResource`.
