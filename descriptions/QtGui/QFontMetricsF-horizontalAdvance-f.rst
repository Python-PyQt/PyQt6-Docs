.. sip:method-description::
    :status: todo
    :pysig: 2b59d303f7633ee1c08c8de09d5143aa
    :realsig: (const QString&,int) const
    :digest: aaf442032e8fa420ce2eb3eb0c36a8f3

Returns the horizontal advance in pixels of the first *length* characters of *text*. If *length* is negative (the default), the entire string is used.

The advance is the distance appropriate for drawing a subsequent character after *text*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.boundingRect`.
