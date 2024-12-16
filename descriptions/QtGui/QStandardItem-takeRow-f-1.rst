.. sip:method-description::
    :status: todo
    :pysig: 599a893f308377a79afc2fa47f788fa2
    :realsig: (int)
    :digest: 8a10bb0a12b716c332690399d663ef47

Removes *row* without deleting the row items, and returns a list of pointers to the removed items. For items in the row that have not been set, the corresponding pointers in the list will be ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.removeRow`, :sip:ref:`~PyQt6.QtGui.QStandardItem.insertRow`, :sip:ref:`~PyQt6.QtGui.QStandardItem.takeColumn`.
