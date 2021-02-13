.. sip:method-description::
    :status: todo
    :pysig: 3eedcfe379a2cd41bb1af4737a9cf52e
    :realsig: (const QRectF&,const QString&,const QTextOption&)
    :digest: 84908595555fc7ca2c7cda8192955480

This is an overloaded function.

Draws the given *text* in the *rectangle* specified using the *option* to control its positioning, direction, and orientation. The options given in *option* override those set on the :sip:ref:`~PyQt6.QtGui.QPainter` object itself.

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-coordinate of *rectangle* is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setPen`.
