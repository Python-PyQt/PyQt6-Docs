.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: 866294b8470bdd0cc5e8cfd3c5746b85

Returns a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ representing the Json document.

The returned variant will be a QVariantList if the document is a QJsonArray and a QVariantMap if the document is a QJsonObject.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QJsonDocument.fromVariant`, :sip:ref:`~PyQt6.QtCore.QJsonValue.toVariant`.
