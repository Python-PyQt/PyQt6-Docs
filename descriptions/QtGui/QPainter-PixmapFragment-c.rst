.. sip:class-description::
    :status: todo
    :brief: This class is used in conjunction with the QPainter::drawPixmapFragments() function to specify how a pixmap, or sub-rect of a pixmap, is drawn
    :digest: fc7cf6a63c7226bdd5e465caa32bdcbc

This class is used in conjunction with the :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmapFragments` function to specify how a pixmap, or sub-rect of a pixmap, is drawn.

The *sourceLeft*, *sourceTop*, *width* and *height* variables are used as a source rectangle within the pixmap passed into the :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmapFragments` function. The variables *x*, *y*, *width* and *height* are used to calculate the target rectangle that is drawn. *x* and *y* denotes the center of the target rectangle. The *width* and *height* in the target rectangle is scaled by the *scaleX* and *scaleY* values. The resulting target rectangle is then rotated *rotation* degrees around the *x*, *y* center point.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmapFragments`.
