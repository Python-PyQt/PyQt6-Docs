.. sip:method-description::
    :status: todo
    :pysig: 599a893f308377a79afc2fa47f788fa2
    :realsig: (int)
    :digest: 61e138f6d581fc3f4d9022aaaea9f34e

Removes the given *row* without deleting the row items, and returns a list of pointers to the removed items. The model releases ownership of the items. For items in the row that have not been set, the corresponding pointers in the list will be ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.takeColumn`.
