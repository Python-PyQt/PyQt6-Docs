.. sip:method-description::
    :status: todo
    :pysig: b8446e1585e0118a477fc1188aecc690
    :realsig: (const QPoint&)
    :digest: 2b62c5811cfe8bac89e0f45bd98049f2

Sets the position of the hot spot relative to the top-left corner of the pixmap used to the point specified by *hotspot*.

**Note:** on X11, the pixmap may not be able to keep up with the mouse movements if the hot spot causes the pixmap to be displayed directly under the cursor.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDrag.hotSpot`.
