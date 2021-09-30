.. sip:class-description::
    :status: todo
    :brief: Defines a circular geographic area
    :digest: 4f2e7f6d587d9bc71ceb1558e0030531

The :sip:ref:`~PyQt6.QtPositioning.QGeoCircle` class defines a circular geographic area.

The circle is defined in terms of a :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` which specifies the center of the circle and a qreal which specifies the radius of the circle in meters.

The circle is considered invalid if the center coordinate is invalid or if the radius is less than zero.

This class is a Q_GADGET since Qt 5.5. It can be `directly used from C++ and QML <https://doc.qt.io/qt-6/positioning-cpp-qml.html#cpp-value-integration-positioning>`_.
