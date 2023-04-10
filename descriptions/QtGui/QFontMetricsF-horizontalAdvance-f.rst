.. sip:method-description::
    :status: todo
    :pysig: 2b59d303f7633ee1c08c8de09d5143aa
    :realsig: (const QString&,int) const
    :digest: dd98000be7cd6a18f197f1064b04d538

Returns the horizontal advance in pixels of the first *length* characters of *text*. If *length* is negative (the default), the entire string is used. The entire length of *text* is analysed even if *length* is substantially shorter.

The advance is the distance appropriate for drawing a subsequent character after *text*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.boundingRect`.
