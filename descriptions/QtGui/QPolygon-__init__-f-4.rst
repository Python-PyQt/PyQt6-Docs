.. sip:method-description::
    :status: todo
    :pysig: 11ca7ca7923551ccb3b5bb995e66b1ee
    :realsig: (const QRect&,bool)
    :digest: a9362e6ebcc541e110bf30040523fbc1

Constructs a polygon from the given *rectangle*. If *closed* is false, the polygon just contains the four points of the rectangle ordered clockwise, otherwise the polygon's fifth point is set to *rectangle*.topLeft().

Note that the bottom-right corner of the rectangle is located at (rectangle.x() + rectangle.width(), rectangle.y() + rectangle.height()).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPolygon.setPoints`.
