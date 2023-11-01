.. sip:method-description::
    :status: todo
    :pysig: ef2891f814183092fd90d48855bc3d25
    :realsig: (const QString&, const QTextOption&) const
    :digest: 8f08e891a13a4b30c543b205dea8a3ff

Returns the bounding rectangle of the characters in the string specified by *text* laid out using *option*. The bounding rectangle always covers at least the set of pixels the text would cover if drawn at (0, 0).

Note that the bounding rectangle may extend to the left of (0, 0), e.g. for italicized fonts, and that the width of the returned rectangle might be different than what the :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance` method returns.

If you want to know the advance width of the string (to lay out a set of strings next to each other), use :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance` instead.

Newline characters are processed as normal characters, *not* as linebreaks.

The height of the bounding rectangle is at least as large as the value returned :sip:ref:`~PyQt6.QtGui.QFontMetricsF.height`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.height`, :sip:ref:`~PyQt6.QtGui.QPainter.boundingRect`.
