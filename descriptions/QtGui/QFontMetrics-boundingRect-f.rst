.. sip:method-description::
    :status: todo
    :pysig: 87b99329d57d55b999bd2bfec9b01ec6
    :realsig: (const QString&) const
    :digest: 60f952ba93fdd3a8b3e33114c1ec6002

Returns the bounding rectangle of the characters in the string specified by *text*. The bounding rectangle always covers at least the set of pixels the text would cover if drawn at (0, 0).

Note that the bounding rectangle may extend to the left of (0, 0), e.g. for italicized fonts, and that the width of the returned rectangle might be different than what the :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` method returns.

If you want to know the advance width of the string (to lay out a set of strings next to each other), use :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` instead.

Newline characters are processed as normal characters, *not* as linebreaks.

The height of the bounding rectangle is at least as large as the value returned by :sip:ref:`~PyQt6.QtGui.QFontMetrics.height`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.height`, :sip:ref:`~PyQt6.QtGui.QPainter.boundingRect`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.tightBoundingRect`.
