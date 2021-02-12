.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 134236a8bf2177f8e35c61b454c32a3c

Ends a row insertion operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRows` in a subclass, you must call this function *after* inserting data into the model's underlying data store.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginInsertRows`.
