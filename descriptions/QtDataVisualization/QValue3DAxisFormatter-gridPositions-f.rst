.. sip:method-description::
    :status: todo
    :pysig: 021dbd5510a963cb43170a72ca7d4949
    :realsig: () const
    :digest: 3c8adba7f6994b0b7875a8e0408760f5

Returns a reference to the array of normalized grid line positions. The default array size is equal to the segment count of the parent axis plus one, but a subclassed implementation of the :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate` method may resize the array differently. The values should be between ``0.0`` (the minimum value) and ``1.0`` (the maximum value), inclusive.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis.segmentCount`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.recalculate`.
