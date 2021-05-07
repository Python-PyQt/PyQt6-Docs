.. sip:method-description::
    :status: todo
    :pysig: 1011e23e4fc82450b79849d3cc359a6e
    :realsig: () const
    :digest: 6b86d10c96b29449d3841180f96221eb

Returns the flags used to describe the item. These determine whether the item can be checked, edited, and selected.

The default value for flags is :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag.ItemIsSelectable` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag.ItemIsUserCheckable` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag.ItemIsEnabled` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag.ItemIsDragEnabled` | :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag.ItemIsDropEnabled`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setFlags`.
