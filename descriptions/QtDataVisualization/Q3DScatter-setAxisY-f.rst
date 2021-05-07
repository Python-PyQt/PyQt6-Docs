.. sip:method-description::
    :status: todo
    :pysig: 6b16365c76467cbb63d7779f3524ef66
    :realsig: (QValue3DAxis*)
    :digest: faafa5edd20323e641833c6cb3ff71e5

Sets *axis* as the active y-axis. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.addAxis` to transfer the ownership of the axis to this graph.

If *axis* is null, a temporary default axis with no labels and an automatically adjusting range is created. This temporary axis is destroyed if another axis is set explicitly to the same orientation.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.axisY`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.releaseAxis`.
