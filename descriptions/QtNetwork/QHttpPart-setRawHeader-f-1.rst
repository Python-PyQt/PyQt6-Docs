.. sip:method-description::
    :status: todo
    :pysig: 9a01ca953cb072293976de4f13623118
    :realsig: (const QByteArray&, const QByteArray&)
    :digest: c6b652de478cc8590946012d7ff9983d

Sets the header *headerName* to be of value *headerValue*. If *headerName* corresponds to a known header (see :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`), the raw format will be parsed and the corresponding "cooked" header will be set as well.

**Note:** Setting the same header twice overrides the previous setting. To accomplish the behaviour of multiple HTTP headers of the same name, you should concatenate the two values, separating them with a comma (",") and set one single raw header.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`, :sip:ref:`~PyQt6.QtNetwork.QHttpPart.setHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader`.
