.. sip:method-description::
    :status: todo
    :pysig: 4d198984cda037ae24fe3f5112568937
    :realsig: (const QModelIndex&,const QModelIndex&) const
    :digest: 94bb5ee97ff9b89b125b182585727b67

Returns ``true`` if the value of the item referred to by the given index *source_left* is less than the value of the item referred to by the given index *source_right*, otherwise returns ``false``.

This function is used as the < operator when sorting, and handles the following `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ types:

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Int`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.UInt`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.LongLong`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.ULongLong`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Float`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Double`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QChar`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QDate`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QTime`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QDateTime`

* :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QString`

Any other type will be converted to a QString using QVariant::toString().

Comparison of QStrings is case sensitive by default; this can be changed using the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sortCaseSensitivity` property.

By default, the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` associated with the :sip:ref:`~PyQt6.QtCore.QModelIndex`\ es is used for comparisons. This can be changed by setting the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sortRole` property.

**Note:** The indices passed in correspond to the source model.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sortRole`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sortCaseSensitivity`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.dynamicSortFilter`.
