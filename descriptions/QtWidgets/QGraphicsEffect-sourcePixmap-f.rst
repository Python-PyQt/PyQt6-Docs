.. sip:method-description::
    :status: todo
    :pysig: 9b820338855f8f542fedff6887eda568
    :realsig: (Qt::CoordinateSystem,QPoint*,QGraphicsEffect::PixmapPadMode) const
    :digest: ca7a542e1d7ca5438048d6f6b5a0649a

Returns a pixmap with the source painted into it.

The *system* specifies which coordinate system to be used for the source. The optional *offset* parameter returns the offset where the pixmap should be painted at using the current painter. For control on how the pixmap is padded use the *mode* parameter.

The returned pixmap is clipped to the current painter's device rectangle when *system* is :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem.DeviceCoordinates`.

Calling this function with :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem.DeviceCoordinates` outside of :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw` will give undefined results, as there is no device context available.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.draw`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.boundingRect`.
