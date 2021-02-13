.. sip:method-description::
    :status: todo
    :pysig: 027e95c41f7a6b3f65f78a5b61a31fab
    :realsig: (QPainter*,const QRectF&)
    :digest: 9cbf878da72ebed3d167f188def5aaf5

Draws the foreground of the scene using *painter*, after the background and all items are drawn. Reimplement this function to provide a custom foreground for this view.

If all you want is to define a color, texture or gradient for the foreground, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setForegroundBrush` instead.

All painting is done in *scene* coordinates. *rect* is the exposed rectangle.

The default implementation fills *rect* using the view's :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.foregroundBrush`. If no such brush is defined (the default), the scene's  function is called instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.drawBackground`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.drawForeground`.
