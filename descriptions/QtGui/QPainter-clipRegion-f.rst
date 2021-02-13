.. sip:method-description::
    :status: todo
    :pysig: 7b302619a1f8d21d9efa913403e8d56b
    :realsig: () const
    :digest: 755b8aefe9e576848806080bbd6ad4c1

Returns the currently set clip region. Note that the clip region is given in logical coordinates.

**Warning:** :sip:ref:`~PyQt6.QtGui.QPainter` does not store the combined clip explicitly as this is handled by the underlying :sip:ref:`~PyQt6.QtGui.QPaintEngine`, so the path is recreated on demand and transformed to the current logical coordinate system. This is potentially an expensive operation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setClipRegion`, :sip:ref:`~PyQt6.QtGui.QPainter.clipPath`, :sip:ref:`~PyQt6.QtGui.QPainter.setClipping`.
