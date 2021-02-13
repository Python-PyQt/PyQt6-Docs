.. sip:method-description::
    :status: todo
    :pysig: 10b73e32ef579338968290bf7f39b35c
    :realsig: (const QRectF&) const
    :digest: ae0f8d7b67552f207790aece20383bf8

Returns the effective bounding rectangle for this effect, given the provided *rect* in the device coordinates. When writing you own custom effect, you must call :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.updateBoundingRect` whenever any parameters are changed that may cause this this function to return a different value.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.sourceBoundingRect`.
