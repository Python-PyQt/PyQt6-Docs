.. sip:method-description::
    :status: todo
    :pysig: dee35a2bcdaa59c6ce9d998a8a3a094d
    :realsig: () const
    :digest: 6b86d10c96b29449d3841180f96221eb

Returns the flags used to describe the item. These determine whether the item can be checked, edited, and selected.

The default value for flags is :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsSelectable` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsUserCheckable` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsEnabled` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsDragEnabled` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsDropEnabled`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setFlags`.
