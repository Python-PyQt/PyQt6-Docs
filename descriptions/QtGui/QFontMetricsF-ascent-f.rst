.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: e6f19729eb4ba7f2ca391a7d53821efa

Returns the ascent of the font.

The ascent of a font is the distance from the baseline to the highest position characters extend to. In practice, some font designers break this rule, e.g. when they put more than one accent on top of a character, or to accommodate a certain character, so it is possible (though rare) that this value will be too small.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.descent`.
