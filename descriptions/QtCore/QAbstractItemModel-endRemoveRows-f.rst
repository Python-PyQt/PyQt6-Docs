.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5fe68a6dfef8e62c0561d3cd714a2469

Ends a row removal operation.

When reimplementing :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows` in a subclass, you must call this function *after* removing data from the model's underlying data store.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginRemoveRows`.
