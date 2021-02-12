.. sip:method-description::
    :status: todo
    :pysig: afbf07365a554bffe7b9fbc375747aca
    :realsig: (int,int,const QModelIndex&)
    :digest: aa10c2067711ccad0b1428ca01521ee3

On models that support this, removes *count* columns starting with the given *column* under parent *parent* from the model.

Returns ``true`` if the columns were successfully removed; otherwise returns ``false``.

The base class implementation does nothing and returns ``false``.

If you implement your own model, you can reimplement this function if you want to support removing. Alternatively, you can provide your own API for altering the data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumn`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endRemoveColumns`.
