.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 5e83162235362fbda856dd340e6be3b3

Returns the descent of the font.

The descent is the distance from the base line to the lowest point characters extend to. (Note that this is different from X, which adds 1 pixel.) In practice, some font designers break this rule, e.g. to accommodate a certain character, so it is possible (though rare) that this value will be too small.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.ascent`.
