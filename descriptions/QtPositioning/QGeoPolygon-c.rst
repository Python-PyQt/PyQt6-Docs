.. sip:class-description::
    :status: todo
    :brief: Defines a geographic polygon
    :digest: 96e2663495a01c49a70fd125ee0bcc05

The :sip:ref:`~PyQt6.QtPositioning.QGeoPolygon` class defines a geographic polygon.

The polygon is defined by an ordered list of :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` objects representing its perimeter.

Each two adjacent elements in this list are intended to be connected together by the shortest line segment of constant bearing passing through both elements. This type of connection can cross the date line in the longitudinal direction, but never crosses the poles.

This is relevant for the calculation of the bounding box returned by :sip:ref:`~PyQt6.QtPositioning.QGeoShape.boundingGeoRectangle` for this shape, which will have the latitude of the top left corner set to the maximum latitude in the path point set. Similarly, the latitude of the bottom right corner will be the minimum latitude in the path point set.

This class is also accessible in QML as `geoPolygon <https://doc.qt.io/qt-6/qml-geopolygon.html>`_.
