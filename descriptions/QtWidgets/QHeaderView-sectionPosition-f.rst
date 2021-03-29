.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: d89be15a707aa17b809141039e960d66

Returns the section position of the given *logicalIndex*, or -1 if the section is hidden. The position is measured in pixels from the first visible item's top-left corner to the top-left corner of the item with *logicalIndex*. The measurement is along the x-axis for horizontal headers and along the y-axis for vertical headers.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionViewportPosition`.
