.. sip:class-description::
    :status: todo
    :brief: Defines a geographical position on the surface of the Earth
    :digest: a0595328411507c7467c3b28214022f6

The :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` class defines a geographical position on the surface of the Earth.

A :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` is defined by latitude, longitude, and optionally, altitude.

Use :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.type` to determine whether a coordinate is a 2D coordinate (has latitude and longitude only) or 3D coordinate (has latitude, longitude and altitude). Use :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.distanceTo` and :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate.azimuthTo` to calculate the distance and bearing between coordinates.

The coordinate values should be specified using the WGS84 datum. For more information on geographical terms see this article on `coordinates <http://en.wikipedia.org/wiki/Geographic_coordinate_system>`_ and another on `geodetic systems <http://en.wikipedia.org/wiki/Geodetic_system>`_ including WGS84.

Azimuth in this context is equivalent to a compass bearing based on true north.

This class is a Q_GADGET since Qt 5.5. It can be `directly used from C++ and QML <https://doc.qt.io/qt-6/positioning-cpp-qml.html#cpp-value-integration-positioning>`_.
