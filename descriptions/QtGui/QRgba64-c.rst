.. sip:class-description::
    :status: todo
    :brief: Struct contains a 64-bit RGB color
    :digest: f80f258378c19c4560c9dedfc1b5d54d

The :sip:ref:`~PyQt6.QtGui.QRgba64` struct contains a 64-bit RGB color.

:sip:ref:`~PyQt6.QtGui.QRgba64` is a 64-bit data-structure containing four 16-bit color channels: Red, green, blue and alpha.

:sip:ref:`~PyQt6.QtGui.QRgba64` can be used as a replacement for QRgb when higher precision is needed. In particular a premultiplied :sip:ref:`~PyQt6.QtGui.QRgba64` can operate on unpremultiplied QRgb without loss of precision except for alpha 0.

.. seealso:: QRgb, :sip:ref:`~PyQt6.QtGui.QColor`.
