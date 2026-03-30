.. sip:method-description::
    :status: todo
    :pysig: d1377f43f219bcec699528c11e609e9c
    :realsig: (const QString&, int) const
    :digest: dd98000be7cd6a18f197f1064b04d538

Returns the horizontal advance in pixels of the first *length* characters of *text*. If *length* is negative (the default), the entire string is used. The entire length of *text* is analysed even if *length* is substantially shorter.

The advance is the distance appropriate for drawing a subsequent character after *text*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.boundingRect`.
