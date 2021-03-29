.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 49ff42a0258437e3beef6c7f8335caaa

Ends a column insertion operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertColumns` in a subclass, you must call this function *after* inserting data into the model's underlying data store.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertColumns`.
