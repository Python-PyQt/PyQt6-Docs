.. sip:method-description::
    :status: todo
    :pysig: 9e70a19e54b399fff7b647e5bfa12d78
    :realsig: (const QModelIndex&) const
    :digest: 76e1fe5103beb804366903223f4e124b

Returns a pointer to the :sip:ref:`~PyQt6.QtGui.QStandardItem` associated with the given *index*.

Calling this function is typically the initial step when processing :sip:ref:`~PyQt6.QtCore.QModelIndex`-based signals from a view, such as :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.activated`. In your slot, you call , with the :sip:ref:`~PyQt6.QtCore.QModelIndex` carried by the signal as argument, to obtain a pointer to the corresponding :sip:ref:`~PyQt6.QtGui.QStandardItem`.

Note that this function will lazily create an item for the index (using :sip:ref:`~PyQt6.QtGui.QStandardItemModel.itemPrototype`), and set it in the parent item's child table, if no item already exists at that index.

If *index* is an invalid index, this function returns ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItemModel.indexFromItem`.
