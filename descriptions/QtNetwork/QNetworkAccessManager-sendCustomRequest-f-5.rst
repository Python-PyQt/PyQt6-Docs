.. sip:method-description::
    :status: todo
    :pysig: e3d916c0f1451044d05868253ce516e7
    :realsig: (const QNetworkRequest&, const QByteArray&, QHttpMultiPart*)
    :digest: 462e7f3d00eded70ba08b4c0688fe5c1

This is an overloaded function.

Sends a custom request to the server identified by the URL of *request*.

Sends the contents of the *multiPart* message to the destination specified by *request*.

This can be used for sending MIME multipart messages for custom verbs.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`, :sip:ref:`~PyQt6.QtNetwork.QHttpPart`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.put`.
