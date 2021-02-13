.. sip:method-description::
    :status: todo
    :pysig: 97355974be616f4828b08ff65fea09d6
    :realsig: (QNetworkRequest::Attribute) const
    :digest: 66c9d68c02a2d18f954bc68562337723

Returns the attribute associated with the code *code*. If the attribute has not been set, it returns an invalid `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ (type :sip:ref:`~PyQt6.QtCore.QMetaType.Type.UnknownType`).

You can expect the default values listed in :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.Attribute` to be applied to the values returned by this function.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkReply.setAttribute`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.Attribute`.
