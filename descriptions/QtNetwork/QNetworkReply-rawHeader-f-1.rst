.. sip:method-description::
    :status: todo
    :pysig: b2cc0c4f8d9f710ef7e89ba9aa900aca
    :realsig: (const QByteArray&) const
    :digest: 9f60b23bad7e21bd00dd3d483d58f68e

Returns the raw contents of the header *headerName* as sent by the remote server. If there is no such header, returns an empty byte array, which may be indistinguishable from an empty header. Use :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.hasRawHeader` to verify if the server sent such header field.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.setRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.hasRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.header`.
