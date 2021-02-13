.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: () const
    :digest: 01fd0cab5fade7f003586bbd50e1d570

Returns the pixel per meter metric for the scrolled widget.

The value is reported for both the x and y axis separately by using a :sip:ref:`~PyQt6.QtCore.QPointF`.

**Note:** Please note that this value should be physically correct. The actual DPI settings that Qt returns for the display may be reported wrongly on purpose by the underlying windowing system, for example on macOS.
