.. sip:method-description::
    :status: todo
    :pysig: 3b11178a0504c6b58aa0e3368b484f58
    :realsig: (int,const QModelIndex&) const
    :digest: e88904aea35d9bca99eee254a74f3f47

Returns ``true`` if all items are selected in the *column* with the given *parent*.

Note that this function is usually faster than calling :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.isSelected` on all items in the same column and that unselectable items are ignored.

**Note:** Since Qt 5.15, the default argument for *parent* is an empty model index.
