.. sip:method-description::
    :status: todo
    :pysig: 22c4dbf8233b3dbf702bcc1a2f66b7b9
    :realsig: (int)
    :digest: e921beb99c1a92c8d4450212bb6dd048

Removes *column* without deleting the column items, and returns a list of pointers to the removed items. For items in the column that have not been set, the corresponding pointers in the list will be ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.removeColumn`, :sip:ref:`~PyQt6.QtGui.QStandardItem.insertColumn`, :sip:ref:`~PyQt6.QtGui.QStandardItem.takeRow`.
