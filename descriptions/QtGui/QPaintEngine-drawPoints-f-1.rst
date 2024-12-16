.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint*,int)
    :digest: 656e1278eec2d71df6f8d4b0731186b4

Draws the first *pointCount* points in the buffer *points*

The default implementation converts the first *pointCount* QPoints in *points* to QPointFs and calls the floating point version of drawPoints.
