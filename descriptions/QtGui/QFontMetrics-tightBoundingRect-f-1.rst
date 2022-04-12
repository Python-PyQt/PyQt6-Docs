.. sip:method-description::
    :status: todo
    :pysig: 1095785b2994d5e5bce82e02293163e0
    :realsig: (const QString&,const QTextOption&) const
    :digest: 4e643d323f067df782fafc7b74e79bdd

Returns a tight bounding rectangle around the characters in the string specified by *text* laid out using *option*. The bounding rectangle always covers at least the set of pixels the text would cover if drawn at (0, 0).

Note that the bounding rectangle may extend to the left of (0, 0), e.g. for italicized fonts, and that the width of the returned rectangle might be different than what the :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` method returns.

If you want to know the advance width of the string (to lay out a set of strings next to each other), use :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` instead.

Newline characters are processed as normal characters, *not* as linebreaks.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.height`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.boundingRect`.
