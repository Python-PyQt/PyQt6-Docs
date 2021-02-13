.. sip:method-description::
    :status: todo
    :pysig: 027e95c41f7a6b3f65f78a5b61a31fab
    :realsig: (QPainter*,const QRectF&)
    :digest: c48a921aac3765fd132e7ff6083243a9

Draws the foreground of the scene using *painter*, after the background and all items have been drawn. Reimplement this function to provide a custom foreground for the scene.

All painting is done in *scene* coordinates. The *rect* parameter is the exposed rectangle.

If all you want is to define a color, texture or gradient for the foreground, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setForegroundBrush` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.drawBackground`, drawItems().
