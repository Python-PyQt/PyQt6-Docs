.. sip:method-description::
    :status: todo
    :pysig: b672d785df50f8c173094cdd46267882
    :realsig: (const QRectF&,const QPixmap&,const QPointF&)
    :digest: ec429b23798b208e59c67e8598371564

Draws a tiled *pixmap*, inside the given *rectangle* with its origin at the given *position*.

Calling drawTiledPixmap() is similar to calling :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap` several times to fill (tile) an area with a pixmap, but is potentially much more efficient depending on the underlying window system.

drawTiledPixmap() will produce the same visual tiling pattern on high-dpi displays (with devicePixelRatio > 1), compared to normal- dpi displays. Set the devicePixelRatio on the *pixmap* to control the tile size. For example, setting it to 2 halves the tile width and height (on both 1x and 2x displays), and produces high-resolution output on 2x displays.

The *position* offset is always in the painter coordinate system, indepentent of display devicePixelRatio.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawPixmap`.
