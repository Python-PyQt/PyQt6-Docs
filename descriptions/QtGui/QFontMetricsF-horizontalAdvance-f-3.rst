.. sip:method-description::
    :status: todo
    :pysig: f45bbac0d74ce8b13949073611a30a2c
    :realsig: (const QString&, int) const
    :digest: dd98000be7cd6a18f197f1064b04d538

Returns the horizontal advance in pixels of the first *length* characters of *text*. If *length* is negative (the default), the entire string is used. The entire length of *text* is analysed even if *length* is substantially shorter.

The advance is the distance appropriate for drawing a subsequent character after *text*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.boundingRect`.
