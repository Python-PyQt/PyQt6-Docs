.. sip:method-description::
    :status: todo
    :pysig: 027e95c41f7a6b3f65f78a5b61a31fab
    :realsig: (QPainter*,const QRectF&)
    :digest: ec3419081547b05f6db46b7f58ebc101

Draws the background of the scene using *painter*, before any items and the foreground are drawn. Reimplement this function to provide a custom background for this view.

If all you want is to define a color, texture or gradient for the background, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setBackgroundBrush` instead.

All painting is done in *scene* coordinates. *rect* is the exposed rectangle.

The default implementation fills *rect* using the view's :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.backgroundBrush`. If no such brush is defined (the default), the scene's  function is called instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.drawForeground`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.drawBackground`.
