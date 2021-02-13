.. sip:method-description::
    :status: todo
    :pysig: fb0ba0763248f760348d1aed171d3d31
    :realsig: (const QMatrix4x4&,const QMatrix4x4&,const QRect&) const
    :digest: 80c9043e3512b18124be2e2649c70c3f

Returns the window coordinates of this vector initially in object/model coordinates using the model view matrix *modelView*, the projection matrix *projection* and the viewport dimensions *viewport*.

When transforming from clip to normalized space, a division by the w component on the vector components takes place. To prevent dividing by 0 if w equals to 0, it is set to 1.

**Note:** the returned y coordinates are in OpenGL orientation. OpenGL expects the bottom to be 0 whereas for Qt top is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D.unproject`.
