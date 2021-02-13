.. sip:method-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: (const QFont&)
    :digest: 5b47588f906029addcca134e52165936

Sets the painter's font to the given *font*.

This font is used by subsequent :sip:ref:`~PyQt6.QtGui.QPainter.drawText` functions. The text color is the same as the pen color.

If you set a font that isn't available, Qt finds a close match. :sip:ref:`~PyQt6.QtGui.QPainter.font` will return what you set using  and :sip:ref:`~PyQt6.QtGui.QPainter.fontInfo` returns the font actually being used (which may be the same).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.font`, :sip:ref:`~PyQt6.QtGui.QPainter.drawText`, Settings.
