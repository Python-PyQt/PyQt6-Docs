.. sip:method-description::
    :status: todo
    :pysig: 80c4e5e7a6745627d4d5b1fe516c3a50
    :realsig: (QSGGeometry*,QSGTexture*,const QRectF&,QRectF,QSGImageNode::TextureCoordinatesTransformMode)
    :digest: d95d9318a1cbb8ab995b43f003ae2db4

Updates the geometry *g* with the *texture*, the coordinates in *rect*, and the texture coordinates from *sourceRect*.

*g* is assumed to be a triangle strip of four vertices of type :sip:ref:`~PyQt6.QtQuick.QSGGeometry.TexturedPoint2D`.

*texCoordMode* is used for normalizing the *sourceRect*.
