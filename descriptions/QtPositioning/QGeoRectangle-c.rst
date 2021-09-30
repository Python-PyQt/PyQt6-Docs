.. sip:class-description::
    :status: todo
    :brief: Defines a rectangular geographic area
    :digest: d151733e1926bc35343f4bb459bf6ac5

The :sip:ref:`~PyQt6.QtPositioning.QGeoRectangle` class defines a rectangular geographic area.

The rectangle is defined in terms of a :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` which specifies the top left coordinate of the rectangle and a :sip:ref:`~PyQt6.QtPositioning.QGeoCoordinate` which specifies the bottom right coordinate of the rectangle.

A geo rectangle is considered invalid if the top left or bottom right coordinates are invalid or if the top left coordinate is south of the bottom right coordinate.

Geo rectangles can never cross the poles.

Several methods behave as though the geo rectangle is defined in terms of a center coordinate, the width of the geo rectangle in degrees and the height of the geo rectangle in degrees.

If the height or center of a geo rectangle is adjusted such that it would cross one of the poles the height is modified such that the geo rectangle touches but does not cross the pole and that the center coordinate is still in the center of the geo rectangle.

This class is a Q_GADGET since Qt 5.5. It can be `directly used from C++ and QML <https://doc.qt.io/qt-6/positioning-cpp-qml.html#cpp-value-integration-positioning>`_.
