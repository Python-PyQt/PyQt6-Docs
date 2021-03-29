.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint*,int)
    :digest: 7bad79f82312d9012747c0e6f351d40d

Draws the first *pointCount* points in the buffer *points*

The default implementation converts the first *pointCount* QPoints in *points* to QPointFs and calls the floating point version of :sip:ref:`~PyQt6.QtGui.QPaintEngine.drawPoints`.
