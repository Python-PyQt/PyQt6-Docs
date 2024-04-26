.. sip:method-description::
    :status: todo
    :pysig: 731d872c21d87206e749c588dc101bf1
    :realsig: (QAnyStringView) const
    :digest: 9f27baebc70dd4639cb6f7e8e1297ec2

Returns the raw form of header *headerName*. If no such header is present, an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is returned, which may be indistinguishable from a header that is present but has no content (use :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.hasRawHeader` to find out if the header exists or not).

Raw headers can be set with :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader` or with :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setHeader`.

**Note:** In Qt versions prior to 6.7, this function took :sip:ref:`~PyQt6.QtCore.QByteArray` only.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.header`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.setRawHeader`.
