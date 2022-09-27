.. sip:method-description::
    :status: todo
    :pysig: b3498ef0751ac0cb503b6f74206b7269
    :realsig: (const QModelIndex&,const QEvent*) const
    :digest: 398ac4cd0492c3ac95e0929d7ecedd70

Returns the SelectionFlags to be used when updating a selection model for the specified *index*. The result depends on the current :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionMode`, and on the user input event *event*, which can be ``nullptr``.

Reimplement this function to define your own selection behavior.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelection`.
