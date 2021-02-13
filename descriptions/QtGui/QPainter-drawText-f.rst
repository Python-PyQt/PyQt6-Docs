.. sip:method-description::
    :status: todo
    :pysig: 5ddb57ee79fa95dfd6c4121b0e1db6d0
    :realsig: (const QPointF&,const QString&)
    :digest: 10dfc1b90a924435aaf7b3b70dd172a8

Draws the given *text* with the currently defined text direction, beginning at the given *position*.

This function does not handle the newline character (\\n), as it cannot break text into multiple lines, and it cannot display the newline character. Use the  overload that takes a rectangle instead if you want to draw multiple lines of text with the newline character, or if you want the text to be wrapped.

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-position is used as the baseline of the font.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setPen`.
