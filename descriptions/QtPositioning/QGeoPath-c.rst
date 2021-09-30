.. sip:class-description::
    :status: todo
    :brief: Defines a geographic path
    :digest: a8cf93e468b8731e6032d60ed797a36b

The :sip:ref:`~PyQt6.QtPositioning.QGeoPath` class defines a geographic path.

The path is defined by an ordered list of :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` objects.

Each two adjacent elements in the path are intended to be connected together by the shortest line segment of constant bearing passing through both elements. This type of connection can cross the dateline in the longitudinal direction, but never crosses the poles.

This is relevant for the calculation of the bounding box returned by :sip:ref:`~PyQt6.QtPositioning.QGeoShape.boundingGeoRectangle` for this shape, which will have the latitude of the top left corner set to the maximum latitude in the path point set. Similarly, the latitude of the bottom right corner will be the minimum latitude in the path point set.

This class is a Q_GADGET. It can be `directly used from C++ and QML <https://doc.qt.io/qt-6/positioning-cpp-qml.html#cpp-value-integration-positioning>`_.

A :sip:ref:`~PyQt6.QtPositioning.QGeoPath` is both invalid and empty if it contains no coordinate.

**Note:** A default constructed :sip:ref:`~PyQt6.QtPositioning.QGeoPath` is both invalid and empty as it does not contain any coordinates.
