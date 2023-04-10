.. sip:method-description::
    :status: todo
    :pysig: 3378edf239f785ea8322be56dc9533d4
    :realsig: (const QColor&,Qt::MaskMode) const
    :digest: ef79421e57c8709d698da765044a1361

Creates and returns a mask for this pixmap based on the given *maskColor*. If the *mode* is :sip:ref:`~PyQt6.QtCore.Qt.MaskMode.MaskInColor`, all pixels matching the maskColor will be transparent. If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.MaskMode.MaskOutColor`, all pixels matching the maskColor will be opaque.

This function is slow because it involves converting to/from a :sip:ref:`~PyQt6.QtGui.QImage`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.createHeuristicMask`.
