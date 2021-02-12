.. sip:method-description::
    :status: todo
    :pysig: afbf07365a554bffe7b9fbc375747aca
    :realsig: (int,int,const QModelIndex&)
    :digest: 3a54183354a5a046417d30452faf4bc4

**Note:** The base class implementation of this function does nothing and returns ``false``.

On models that support this, inserts *count* rows into the model before the given *row*. Items in the new row will be children of the item represented by the *parent* model index.

If *row* is 0, the rows are prepended to any existing rows in the parent.

If *row* is :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount`, the rows are appended to any existing rows in the parent.

If *parent* has no children, a single column with *count* rows is inserted.

Returns ``true`` if the rows were successfully inserted; otherwise returns ``false``.

If you implement your own model, you can reimplement this function if you want to support insertions. Alternatively, you can provide your own API for altering the data. In either case, you will need to call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertRows` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertRows` to notify other components that the model has changed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endInsertRows`.
