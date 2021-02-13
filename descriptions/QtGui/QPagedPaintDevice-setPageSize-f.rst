.. sip:method-description::
    :status: todo
    :pysig: ea7f51b29bb5b9fdca8d50afb4afc621
    :realsig: (const QPageSize&)
    :digest: 60a015e02b7bc423b309953343413b58

Sets the page size to *pageSize*.

To get the current :sip:ref:`~PyQt6.QtGui.QPageSize` use :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.pageSize().

You should call this before calling :sip:ref:`~PyQt6.QtGui.QPainter.begin`, or immediately before calling :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` to apply the new page size to a new page. You should not call any painting methods between a call to  and :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.newPage` as the wrong paint metrics may be used.

Returns true if the page size was successfully set to *pageSize*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`.
