.. sip:method-description::
    :status: todo
    :pysig: 7c1fb21a2ddb830adbc1d9f648f94928
    :realsig: (QSGGeometry*,const QRectF&,const QRectF&)
    :digest: 736444a20155ae154cf63cccf6bbd2c8

Updates the geometry *g* with the coordinates in *rect* and texture coordinates from *textureRect*.

*textureRect* should be in normalized coordinates.

*g* is assumed to be a triangle strip of four vertices of type :sip:ref:`~PyQt6.QtQuick.QSGGeometry.TexturedPoint2D`.
