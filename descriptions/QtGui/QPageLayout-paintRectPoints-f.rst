.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: () const
    :digest: ad4b51d567c06006bcd51570bd859bb3

Returns the paintable rectangle in rounded Postscript Points (1/72 of an inch).

The paintable rectangle takes into account the page size, orientation and margins.

If the :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` mode is set then the :sip:ref:`~PyQt6.QtGui.QPageLayout.fullRect` is returned and the margins must be manually managed.
