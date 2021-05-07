.. sip:method-description::
    :status: todo
    :pysig: 6b16365c76467cbb63d7779f3524ef66
    :realsig: (QValue3DAxis*)
    :digest: 76bf7fba8715b2720aab94beab377c2b

Sets *axis* as the active x-axis. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.addAxis` to transfer the ownership of the axis to this graph.

If *axis* is null, a temporary default axis with no labels and an automatically adjusting range is created. This temporary axis is destroyed if another axis is set explicitly to the same orientation.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.axisX`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter.releaseAxis`.
