.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: cdc071d1f3f9145f1f4cbeff14d91041

Sets the paragraph's heading *level*, where 1 is the highest-level heading type (usually with the largest possible heading font size), and increasing values are progressively deeper into the document (and usually with smaller font sizes). For example when reading an HTML H1 tag, the heading level is set to 1. Setting the heading level does not automatically change the font size; however :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.fromHtml` sets both the heading level and the font size simultaneously.

If the paragraph is not a heading, the level should be set to 0 (the default).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.headingLevel`.
