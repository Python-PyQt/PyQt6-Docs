.. sip:method-description::
    :status: todo
    :pysig: eb479108903ac2285ca85d2c9f985e8a
    :realsig: (QPageLayout::Unit) const
    :digest: bcb0a9c82077ed43706ce04918257bd9

Returns the page rectangle in the required *units*.

The paintable rectangle takes into account the page size, orientation and margins.

If the :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` mode is set then the :sip:ref:`~PyQt6.QtGui.QPageLayout.fullRect` is returned and the margins must be manually managed.
