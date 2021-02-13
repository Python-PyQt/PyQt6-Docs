.. sip:method-description::
    :status: todo
    :pysig: 3ffc598e8f8ea2d4abdfd08def3e377f
    :realsig: (QNetworkRequest::KnownHeaders) const
    :digest: 7b07875455a39db63d4e0bf7e4b713b1

Returns the value of the known network header *header* if it is in use for this proxy. If it is not present, returns `QVariant() <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ (i.e., an invalid variant).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.rawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setHeader`.
