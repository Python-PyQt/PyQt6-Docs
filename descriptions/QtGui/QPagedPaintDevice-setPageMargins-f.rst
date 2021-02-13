.. sip:method-description::
    :status: todo
    :pysig: c22204d554371ca48d88c7e18f1b490c
    :realsig: (const QMarginsF&,QPageLayout::Unit)
    :digest: 85acfd0acee3ccf0a819dc26f0f8258d

Set the page *margins* defined in the given *units*.

You should call this before calling :sip:ref:`~PyQt6.QtGui.QPainter.begin`, or immediately before calling :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` to apply the new margins to a new page. You should not call any painting methods between a call to  and :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` as the wrong paint metrics may be used.

To get the current page margins use :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.margins().

Returns true if the page margins were successfully set to *margins*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.
