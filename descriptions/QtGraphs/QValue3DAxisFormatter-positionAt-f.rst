.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (float) const
    :digest: 4e51e328dfe946d9b5af1a080de80d21

Returns the normalized position along the axis for the given *value*. The returned value should be between ``0.0`` (the minimum value) and ``1.0`` (the maximum value), inclusive, if the value is within the parent axis range.

Reimplement this method if the position cannot be resolved by linear interpolation between the parent axis minimum and maximum values.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QValue3DAxisFormatter.recalculate`, :sip:ref:`~PyQt6.QtGraphs.QValue3DAxisFormatter.valueAt`.
