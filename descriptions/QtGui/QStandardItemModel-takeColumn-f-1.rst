.. sip:method-description::
    :status: todo
    :pysig: 599a893f308377a79afc2fa47f788fa2
    :realsig: (int)
    :digest: 6948abf39224350aec81ab57c4db10c9

Removes the given *column* without deleting the column items, and returns a list of pointers to the removed items. The model releases ownership of the items. For items in the column that have not been set, the corresponding pointers in the list will be ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.takeRow`.
