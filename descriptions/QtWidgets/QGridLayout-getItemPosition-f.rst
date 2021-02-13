.. sip:method-description::
    :status: todo
    :pysig: c2a647d5516b1918d5a328f3ea644957
    :realsig: (int,int*,int*,int*,int*) const
    :digest: 5d3f4cb3260970529c069ca0b13cfabc

Returns the position information of the item with the given *index*.

The variables passed as *row* and *column* are updated with the position of the item in the layout, and the *rowSpan* and *columnSpan* variables are updated with the vertical and horizontal spans of the item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGridLayout.itemAtPosition`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.itemAt`.
