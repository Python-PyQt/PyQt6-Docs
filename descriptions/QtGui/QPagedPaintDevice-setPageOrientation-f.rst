.. sip:method-description::
    :status: todo
    :pysig: 3ca50bf45077dee8645998013b2e8367
    :realsig: (QPageLayout::Orientation)
    :digest: c20ebbe687a1ca47554cc3f70a19e80e

Sets the page *orientation*.

The page orientation is used to define the orientation of the page size when obtaining the page rect.

You should call this before calling :sip:ref:`~PyQt6.QtGui.QPainter.begin`, or immediately before calling :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` to apply the new orientation to a new page. You should not call any painting methods between a call to  and :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` as the wrong paint metrics may be used.

To get the current :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation` use :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.orientation().

Returns true if the page orientation was successfully set to *orientation*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.
