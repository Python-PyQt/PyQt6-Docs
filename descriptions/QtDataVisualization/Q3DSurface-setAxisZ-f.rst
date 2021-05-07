.. sip:method-description::
    :status: todo
    :pysig: 6b16365c76467cbb63d7779f3524ef66
    :realsig: (QValue3DAxis*)
    :digest: 708d1fa947bcb7e2afe3e79aa67a2e90

Sets *axis* as the active z-axis. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.addAxis` to transfer the ownership of the axis to this graph.

If *axis* is null, a temporary default axis with no labels and an automatically adjusting range is created.

This temporary axis is destroyed if another axis is set explicitly to the same orientation.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.axisZ`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface.releaseAxis`.
