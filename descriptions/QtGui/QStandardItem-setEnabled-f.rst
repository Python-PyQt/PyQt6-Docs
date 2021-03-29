.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 068d3451afadf5657bf53110926c794c

Sets whether the item is enabled. If *enabled* is true, the item is enabled, meaning that the user can interact with the item; if *enabled* is false, the user cannot interact with the item.

This flag takes precedence over the other item flags; e.g. if an item is not enabled, it cannot be selected by the user, even if the :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsSelectable` flag has been set.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.isEnabled`, :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags.ItemIsEnabled`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setFlags`.
