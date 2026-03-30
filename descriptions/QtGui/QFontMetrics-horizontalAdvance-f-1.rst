.. sip:method-description::
    :status: todo
    :pysig: a341d2f440482b4a1468b57bab3a2066
    :realsig: (const QString&, int) const
    :digest: c650b31c9592b9edaaa305950915aa53

Returns the horizontal advance in pixels of the first *len* characters of *text*. If *len* is negative (the default), the entire string is used. The entire length of *text* is analysed even if *len* is substantially shorter.

This is the distance appropriate for drawing a subsequent character after *text*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.boundingRect`.
