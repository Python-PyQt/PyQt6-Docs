.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: () const
    :digest: 631ebb2ea260e1aaa6bc6f6e9f07cf62

Returns the page rectangle in the current layout units.

The paintable rectangle takes into account the page size, orientation and margins.

If the :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` mode is set then the :sip:ref:`~PyQt6.QtGui.QPageLayout.fullRect` is returned and the margins must be manually managed.
