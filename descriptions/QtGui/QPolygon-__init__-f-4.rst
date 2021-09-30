.. sip:method-description::
    :status: todo
    :pysig: 11ca7ca7923551ccb3b5bb995e66b1ee
    :realsig: (const QRect&,bool)
    :digest: 3fec0ff097d2ca02d6c7d4f6c9bc40db

Constructs a polygon from the given *rectangle*. If *closed* is false, the polygon just contains the four points of the rectangle ordered clockwise, otherwise the polygon's fifth point is set to *rectangle*.`topLeft() <https://doc.qt.io/qt-6/qml-georectangle.html#topleft>`_.

Note that the bottom-right corner of the rectangle is located at (rectangle.x() + rectangle.`width() <https://doc.qt.io/qt-6/qml-geopath.html#width>`_, rectangle.y() + rectangle.`height() <https://doc.qt.io/qt-6/qml-georectangle.html#height>`_).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPolygon.setPoints`.
