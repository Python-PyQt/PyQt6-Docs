.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0269d716d9f47f397058a1816a6aaebe

Ends a column removal operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumns` in a subclass, you must call this function *after* removing data from the model's underlying data store.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveColumns`.
