.. sip:method-description::
    :status: todo
    :pysig: 3b11178a0504c6b58aa0e3368b484f58
    :realsig: (int,const QModelIndex&)
    :digest: 80953a239a67158aab91dc1f52b03b41

Removes the given *row* from the child items of the *parent* specified.

Returns ``true`` if the row is removed; otherwise returns ``false``.

This is a convenience function that calls :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`. The :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` implementation of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows` does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeRows`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.removeColumn`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.insertRow`.
