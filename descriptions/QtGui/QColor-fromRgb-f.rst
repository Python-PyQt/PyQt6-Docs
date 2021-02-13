.. sip:method-description::
    :status: todo
    :pysig: c33d5184657a637ea20373abf50000d2
    :realsig: (QRgb)
    :digest: d7a92a3000fb92cb6d675d5232a61437

Static convenience function that returns a :sip:ref:`~PyQt6.QtGui.QColor` constructed from the given QRgb value *rgb*.

The alpha component of *rgb* is ignored (i.e. it is automatically set to 255), use the :sip:ref:`~PyQt6.QtGui.QColor.fromRgba` function to include the alpha-channel specified by the given QRgb value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.fromRgba`, :sip:ref:`~PyQt6.QtGui.QColor.fromRgbF`, :sip:ref:`~PyQt6.QtGui.QColor.toRgb`, :sip:ref:`~PyQt6.QtGui.QColor.isValid`.
