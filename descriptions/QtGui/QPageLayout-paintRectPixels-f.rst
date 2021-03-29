.. sip:method-description::
    :status: todo
    :pysig: f911a06648ba49152a2583b34c48ac44
    :realsig: (int) const
    :digest: f74c95d89b7c7a0dddd2a342dd075aa4

Returns the paintable rectangle in rounded device pixels for the given *resolution*.

The paintable rectangle takes into account the page size, orientation and margins.

If the :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` mode is set then the :sip:ref:`~PyQt6.QtGui.QPageLayout.fullRect` is returned and the margins must be manually managed.
