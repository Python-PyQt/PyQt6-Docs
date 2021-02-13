.. sip:method-description::
    :status: todo
    :pysig: 66d9553835d5f405b7d075bb63489910
    :realsig: (const QVariant&,const QLocale&) const
    :digest: 06e32012a5260cbb7357560e0e675a1d

This function returns the string that the delegate will use to display the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` of the model in *locale*. *value* is the value of the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` provided by the model.

The default implementation uses the :sip:ref:`~PyQt6.QtCore.QLocale.toString` to convert *value* into a QString.

This function is not called for empty model indices, i.e., indices for which the model returns an invalid `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`.
