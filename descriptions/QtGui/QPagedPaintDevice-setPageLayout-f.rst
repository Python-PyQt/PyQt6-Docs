.. sip:method-description::
    :status: todo
    :pysig: 8c57a1d209b1b884dab5be07a505871d
    :realsig: (const QPageLayout&)
    :digest: a8327a2dc13c6ec5264c7c985eb3fe62

Sets the page layout to *newPageLayout*.

You should call this before calling :sip:ref:`~PyQt6.QtGui.QPainter.begin`, or immediately before calling :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` to apply the new page layout to a new page. You should not call any painting methods between a call to  and :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` as the wrong paint metrics may be used.

Returns true if the page layout was successfully set to *newPageLayout*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.
