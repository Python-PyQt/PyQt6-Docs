.. sip:method-description::
    :status: todo
    :pysig: bae26d3b9414603fc51960caae2a69a5
    :realsig: () const
    :digest: b30c8f9e793ecec5a6081649a3912a4a

Returns a bounding shape which represents the recommended region to display when viewing this location.

For example, a building's location may have a region centered around the building, but the region is large enough to show it's immediate surrounding geographical context.

**Note:** This method was introduced in Qt6 instead of boundingBox() method. It returns a :sip:ref:`~PyQt6.QtPositioning.QGeoShape` instead of a :sip:ref:`~PyQt6.QtPositioning.QGeoRectangle`. Use :sip:ref:`~PyQt6.QtPositioning.QGeoShape.boundingGeoRectangle` to obtain a bounding :sip:ref:`~PyQt6.QtPositioning.QGeoRectangle` for the shape.

.. seealso:: :sip:ref:`~PyQt6.QtPositioning.QGeoLocation.setBoundingShape`.
