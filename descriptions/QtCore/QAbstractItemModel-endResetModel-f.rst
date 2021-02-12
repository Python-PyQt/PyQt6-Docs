.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9f8ece8652b7c2ff99e1a6d9333ddcf3

Completes a model reset operation.

You must call this function after resetting any internal data structure in your model or proxy model.

This function emits the signal :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelReset`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.beginResetModel`.
