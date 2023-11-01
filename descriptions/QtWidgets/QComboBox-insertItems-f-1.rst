.. sip:method-description::
    :status: todo
    :pysig: decef4612d25a2425f5232cc2139aab9
    :realsig: (int, const QStringList&)
    :digest: 7923f72a61a61e8849c8b13b7e867b36

Inserts the strings from the *list* into the combobox as separate items, starting at the *index* specified.

If the index is equal to or higher than the total number of items, the new items are appended to the list of existing items. If the index is zero or negative, the new items are prepended to the list of existing items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.insertItem`.
