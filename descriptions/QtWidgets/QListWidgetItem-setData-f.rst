.. sip:method-description::
    :status: todo
    :pysig: 929edda6a97571ebce7151ff0802751f
    :realsig: (int,const QVariant&)
    :digest: de307c0e694673a60e093bb0e68ece39

Sets the data for a given *role* to the given *value*. Reimplement this function if you need extra roles or special behavior for certain roles.

**Note:** The default implementation treats :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` as referring to the same data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`, :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.data`.
