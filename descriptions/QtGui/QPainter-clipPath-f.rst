.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: 310a9d9727d846a20e7d8dd6e862b457

Returns the current clip path in logical coordinates.

**Warning:** :sip:ref:`~PyQt6.QtGui.QPainter` does not store the combined clip explicitly as this is handled by the underlying :sip:ref:`~PyQt6.QtGui.QPaintEngine`, so the path is recreated on demand and transformed to the current logical coordinate system. This is potentially an expensive operation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setClipPath`, :sip:ref:`~PyQt6.QtGui.QPainter.clipRegion`, :sip:ref:`~PyQt6.QtGui.QPainter.setClipping`.
