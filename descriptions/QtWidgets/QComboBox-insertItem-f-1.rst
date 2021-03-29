.. sip:method-description::
    :status: todo
    :pysig: 268d4dc00b7ab9511e8457aa31d31454
    :realsig: (int,const QIcon&,const QString&,const QVariant&)
    :digest: 99c6bb296302feffbbb69e24889648d8

Inserts the *icon*, *text* and *userData* (stored in the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.UserRole`) into the combobox at the given *index*.

If the index is equal to or higher than the total number of items, the new item is appended to the list of existing items. If the index is zero or negative, the new item is prepended to the list of existing items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QComboBox.insertItems`.
