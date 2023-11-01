.. sip:method-description::
    :status: todo
    :pysig: 9a01ca953cb072293976de4f13623118
    :realsig: (const QByteArray&, const QByteArray&)
    :digest: ba2384aee7d5a3f61e1860f348e96a50

Sets the raw header *headerName* to be of value *value*. If *headerName* was previously set, it is overridden. Multiple HTTP headers of the same name are functionally equivalent to one single header with the values concatenated, separated by commas.

If *headerName* matches a known header, the value *value* will be parsed and the corresponding parsed form will also be set.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.rawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.header`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.setHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader`.
