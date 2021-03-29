.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: 52c6abf7856cf3fbe246a1ca16e77dbc

Returns the height size hint for the specified *row* or -1 if there is no model.

The returned height is calculated using the size hints of the given *row*'s items, i.e. the returned value is the maximum height among the items. Note that to control the height of a row, you must reimplement the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.sizeHint` function.

This function is used in views with a vertical header to find the size hint for a header section based on the contents of the given *row*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.sizeHintForColumn`.
