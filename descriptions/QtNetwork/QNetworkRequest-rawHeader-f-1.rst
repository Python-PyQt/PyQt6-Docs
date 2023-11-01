.. sip:method-description::
    :status: todo
    :pysig: b2cc0c4f8d9f710ef7e89ba9aa900aca
    :realsig: (const QByteArray&) const
    :digest: 3d547cd6962f286a22f67dfeb65e51de

Returns the raw form of header *headerName*. If no such header is present, an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is returned, which may be indistinguishable from a header that is present but has no content (use :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.hasRawHeader` to find out if the header exists or not).

Raw headers can be set with :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader` or with :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHeader`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.header`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader`.
