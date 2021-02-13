.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: fdda7100fe63e9d95103abc7d3b73be5

Returns the descent of the font.

The descent is the distance from the base line to the lowest point characters extend to. (Note that this is different from X, which adds 1 pixel.) In practice, some font designers break this rule, e.g. to accommodate an unusual character in an exotic language, so it is possible (though rare) that this value will be too small.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.ascent`.
