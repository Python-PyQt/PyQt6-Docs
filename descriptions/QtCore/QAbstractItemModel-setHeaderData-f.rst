.. sip:method-description::
    :status: todo
    :pysig: 76850491c55fabde5c581ffe31a4aa7e
    :realsig: (int,Qt::Orientation,const QVariant&,int)
    :digest: 375e60ead755a7a84e0258aedf557638

Sets the data for the given *role* and *section* in the header with the specified *orientation* to the *value* supplied.

Returns ``true`` if the header's data was updated; otherwise returns ``false``.

When reimplementing this function, the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerDataChanged` signal must be emitted explicitly.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerData`.
