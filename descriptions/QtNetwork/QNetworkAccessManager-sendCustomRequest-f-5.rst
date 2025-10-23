.. sip:method-description::
    :status: todo
    :pysig: e3d916c0f1451044d05868253ce516e7
    :realsig: (const QNetworkRequest&, const QByteArray&, QHttpMultiPart*)
    :digest: 98797bb81cc1030a244630db9c5711d5

Sends a custom request to the server identified by the URL of *request*.

Sends the contents of the *multiPart* message to the destination specified by *request*.

This can be used for sending MIME multipart messages for custom verbs.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`, :sip:ref:`~PyQt6.QtNetwork.QHttpPart`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`.
