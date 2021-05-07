.. sip:method-description::
    :status: todo
    :pysig: 021dbd5510a963cb43170a72ca7d4949
    :realsig: () const
    :digest: 7d5017a3ed21b82d9f7f1ea74a3995ac

Returns a reference to the array of normalized subgrid line positions. The default array size is equal to the segment count of the parent axis times the sub-segment count of the parent axis minus one, but a subclassed implementation of the :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate` method may resize the array differently. The values should be between ``0.0`` (the minimum value) and ``1.0`` (the maximum value), inclusive.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.segmentCount`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.subSegmentCount`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate`.
