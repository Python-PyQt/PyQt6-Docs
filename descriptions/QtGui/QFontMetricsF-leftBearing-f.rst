.. sip:method-description::
    :status: todo
    :pysig: fe16b9ee4a375a9a3a3b8330a3aef226
    :realsig: (QChar) const
    :digest: dc286daaa1fd1d14f11758652cc339e3

Returns the left bearing of character *ch* in the font.

The left bearing is the right-ward distance of the left-most pixel of the character from the logical origin of the character. This value is negative if the pixels of the character extend to the left of the logical origin.

See :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance` for a graphical description of this metric.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.rightBearing`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.minLeftBearing`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance`.
