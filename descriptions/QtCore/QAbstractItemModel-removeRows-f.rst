.. sip:method-description::
    :status: todo
    :pysig: afbf07365a554bffe7b9fbc375747aca
    :realsig: (int,int,const QModelIndex&)
    :digest: be1cf1a070e3842ed3e31aca9286d33f

On models that support this, removes *count* rows starting with the given *row* under parent *parent* from the model.

Returns ``true`` if the rows were successfully removed; otherwise returns ``false``.

The base class implementation does nothing and returns ``false``.

If you implement your own model, you can reimplement this function if you want to support removing. Alternatively, you can provide your own API for altering the data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRow`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endRemoveRows`.
