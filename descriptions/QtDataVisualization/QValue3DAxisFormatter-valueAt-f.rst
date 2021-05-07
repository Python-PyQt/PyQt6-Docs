.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (float) const
    :digest: f57b5b0b46919a0ec40a458d63d2d28e

Returns the value at the normalized *position* along the axis. The *position* value should be between ``0.0`` (the minimum value) and ``1.0`` (the maximum value), inclusive, to obtain values within the parent axis range.

Reimplement this method if the value cannot be resolved by linear interpolation between the parent axis minimum and maximum values.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.positionAt`.
