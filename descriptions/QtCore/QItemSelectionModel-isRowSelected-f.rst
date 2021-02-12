.. sip:method-description::
    :status: todo
    :pysig: 3b11178a0504c6b58aa0e3368b484f58
    :realsig: (int,const QModelIndex&) const
    :digest: 383eaf42ee6f9b5369cbc427458ce230

Returns ``true`` if all items are selected in the *row* with the given *parent*.

Note that this function is usually faster than calling :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.isSelected` on all items in the same row and that unselectable items are ignored.

**Note:** Since Qt 5.15, the default argument for *parent* is an empty model index.
