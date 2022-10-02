.. sip:method-description::
    :status: todo
    :pysig: 6bbc4e60312c393fcd75f387046074fe
    :realsig: (const QModelIndex&) const
    :digest: c80a471abb2fe3ac669ebf042bce0c0f

Returns ``true`` if *parent* has any children; otherwise returns ``false``.

Use :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.rowCount` on the parent to find out the number of children.

Note that it is undefined behavior to report that a particular index hasChildren with this method if the same index has the flag :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag.ItemNeverHasChildren` set.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.parent`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.index`.
