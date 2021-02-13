.. sip:method-description::
    :status: todo
    :pysig: e27247e5b452ce98dcfc93f19679f890
    :realsig: () const
    :digest: 7375d668f7933c2d2a41748586ab63d4

Returns the matrix that transforms from logical coordinates to device coordinates of the platform dependent paint device.

This function is *only* needed when using platform painting commands on the platform dependent handle (Qt::HANDLE), and the platform does not do transformations nativly.

The :sip:ref:`~PyQt6.QtGui.QPaintEngine.PaintEngineFeatures` enum can be queried to determine whether the platform performs the transformations or not.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.worldTransform`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.hasFeature`.
