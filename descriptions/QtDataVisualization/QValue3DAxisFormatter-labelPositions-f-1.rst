.. sip:method-description::
    :status: todo
    :pysig: 78e43d381ff7864fe31ea99d779fe79f
    :realsig: () const
    :digest: cc8169d496e9eac576e4b2c8e19d3784

Returns a reference to the array of normalized label positions. The default array size is equal to the segment count of the parent axis plus one, but a subclassed implementation of the :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate` method may resize the array differently. The values should be between ``0.0`` (the minimum value) and ``1.0`` (the maximum value), inclusive. By default, the label at the index zero corresponds to the minimum value of the axis.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.segmentCount`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DAxis.labels`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate`.
