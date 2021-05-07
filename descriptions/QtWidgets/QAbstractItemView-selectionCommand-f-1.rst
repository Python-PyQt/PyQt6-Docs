.. sip:method-description::
    :status: todo
    :pysig: b3498ef0751ac0cb503b6f74206b7269
    :realsig: (const QModelIndex&,const QEvent*) const
    :digest: 54eb0381b045e77feb84b24ac6554940

Returns the SelectionFlags to be used when updating a selection with to include the *index* specified. The *event* is a user input event, such as a mouse or keyboard event.

Reimplement this function to define your own selection behavior.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelection`.
