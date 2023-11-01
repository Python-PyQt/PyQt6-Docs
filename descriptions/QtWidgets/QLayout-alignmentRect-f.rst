.. sip:method-description::
    :status: todo
    :pysig: 9b844015e1302619c8f96ba59db1d3aa
    :realsig: (const QRect&) const
    :digest: c48c150489f60feaaf2c21b847955564

Returns the rectangle that should be covered when the geometry of this layout is set to *r*, provided that this layout supports :sip:ref:`~PyQt6.QtWidgets.QLayout.setAlignment`.

The result is derived from sizeHint() and :sip:ref:`~PyQt6.QtWidgets.QLayout.expandingDirections`. It is never larger than *r*.
