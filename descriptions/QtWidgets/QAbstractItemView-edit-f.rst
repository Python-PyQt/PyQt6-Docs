.. sip:method-description::
    :status: todo
    :pysig: af193f7da54d4df813f044d1a85c747b
    :realsig: (const QModelIndex&)
    :digest: 07da8362720cb3000ee7f4f81d882fef

Starts editing the item corresponding to the given *index* if it is editable.

Note that this function does not change the current index. Since the current index defines the next and previous items to edit, users may find that keyboard navigation does not work as expected. To provide consistent navigation behavior, call :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setCurrentIndex` before this function with the same model index.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QModelIndex.flags`.
