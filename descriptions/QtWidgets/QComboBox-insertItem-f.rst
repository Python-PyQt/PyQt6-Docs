.. sip:method-description::
    :status: todo
    :pysig: 66c5319cced2612166775d1410cfb025
    :realsig: (int, const QString&, const QVariant&)
    :digest: 26d8daf98265dd9db57d8fd5f7afecf2

Inserts the *text* and *userData* (stored in the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.UserRole`) into the combobox at the given *index*.

If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items. If the index is zero or negative, the new item is prepended to the list of existing items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.insertItems`.
