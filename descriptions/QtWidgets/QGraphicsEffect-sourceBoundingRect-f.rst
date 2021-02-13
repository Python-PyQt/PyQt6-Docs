.. sip:method-description::
    :status: todo
    :pysig: 0e493561880517aec6fa4883677fe64f
    :realsig: (Qt::CoordinateSystem) const
    :digest: be46109fad2d3c4d7e25387394f05f30

Returns the bounding rectangle of the source mapped to the given *system*.

Calling this function with :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem.DeviceCoordinates` outside of :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw` will give undefined results, as there is no device context available.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw`.
