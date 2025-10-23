.. sip:method-description::
    :status: todo
    :pysig: eb4d760bdcf06e56b26ba10ba3eeb974
    :realsig: (const QRectF&, const QString&, const QTextOption&)
    :digest: be2f711b942606479c3d2a6dbf03678d

Draws the given *text* in the *rectangle* specified using the *option* to control its positioning, direction, and orientation. The options given in *option* override those set on the :sip:ref:`~PyQt6.QtGui.QPainter` object itself.

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-coordinate of *rectangle* is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setPen`.
