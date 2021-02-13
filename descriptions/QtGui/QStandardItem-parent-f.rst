.. sip:method-description::
    :status: todo
    :pysig: dda4d4157806d9fb40b7394b87b3266a
    :realsig: () const
    :digest: e535c1cf71db06015e4263801411c826

Returns the item's parent item, or ``nullptr`` if the item has no parent.

**Note:** For toplevel items  returns ``nullptr``. To receive toplevel item's parent use :sip:ref:`~PyQt6.QtGui.QStandardItemModel.invisibleRootItem` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.child`, :sip:ref:`~PyQt6.QtGui.QStandardItemModel.invisibleRootItem`.
