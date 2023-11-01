.. sip:method-description::
    :status: todo
    :pysig: 140d0f6bb5bdafa8a9be72121a5d9996
    :realsig: (const QVariant&)
    :digest: e9c0b2111cd32d1c07f8f619a524ada9

Creates a :sip:ref:`~PyQt6.QtCore.QJsonDocument` from the :sip:ref:`~PyQt6.QtCore.QVariant` *variant*.

If the *variant* contains any other type than a QVariantMap, QVariantHash, QVariantList or QStringList, the returned document is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QJsonDocument.toVariant`.
