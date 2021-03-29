.. sip:method-description::
    :status: todo
    :pysig: 027e95c41f7a6b3f65f78a5b61a31fab
    :realsig: (QPainter*,const QRectF&)
    :digest: 211c0219f1fcb909a2ccd9c43895856b

Draws the background of the scene using *painter*, before any items and the foreground are drawn. Reimplement this function to provide a custom background for the scene.

All painting is done in *scene* coordinates. The *rect* parameter is the exposed rectangle.

If all you want is to define a color, texture, or gradient for the background, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setBackgroundBrush` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.drawForeground`, drawItems().
