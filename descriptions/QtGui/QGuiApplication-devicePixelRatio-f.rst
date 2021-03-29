.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: a01692d076cd60716136330a61b11750

Returns the highest screen device pixel ratio found on the system. This is the ratio between physical pixels and device-independent pixels.

Use this function only when you don't know which window you are targeting. If you do know the target window, use :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.devicePixelRatio`.
