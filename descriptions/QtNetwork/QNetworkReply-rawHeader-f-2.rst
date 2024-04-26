.. sip:method-description::
    :status: todo
    :pysig: 731d872c21d87206e749c588dc101bf1
    :realsig: (QAnyStringView) const
    :digest: 8197fd5b803da147daeb4eee2be0cece

Returns the raw contents of the header *headerName* as sent by the remote server. If there is no such header, returns an empty byte array, which may be indistinguishable from an empty header. Use :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.hasRawHeader` to verify if the server sent such header field.

**Note:** In Qt versions prior to 6.7, this function took :sip:ref:`~PyQt6.QtCore.QByteArray` only.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.setRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.hasRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.header`.
