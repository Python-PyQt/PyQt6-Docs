.. sip:signal-description::
    :status: todo
    :pysig: b15f45f67a53baacc03b330e9ed8c940
    :realsig: (Qt::Orientation,int,int)
    :digest: c35c60354dbf6ca89bcb0661a60585d5

This signal is emitted whenever a header is changed. The *orientation* indicates whether the horizontal or vertical header has changed. The sections in the header from the *first* to the *last* need to be updated.

When reimplementing the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setHeaderData` function, this signal must be emitted explicitly.

If you are changing the number of columns or rows you do not need to emit this signal, but use the begin/end functions (refer to the section on subclassing in the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class description for details).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setHeaderData`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged`.
