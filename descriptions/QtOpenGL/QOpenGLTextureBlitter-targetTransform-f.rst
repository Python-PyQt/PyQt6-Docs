.. sip:method-description::
    :status: todo
    :pysig: 141559083d0df002c06f5b914bdde3ef
    :realsig: (const QRectF&,const QRect&)
    :digest: 48c99d4ee0295d2ce0b0c03a280ea379

Calculates a target transform suitable for :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit`.

*target* is the target rectangle in pixels. *viewport* describes the source dimensions and will in most cases be set to (0, 0, image width, image height).

For unscaled output the size of *target* and *viewport* should match.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLTextureBlitter.blit`.
