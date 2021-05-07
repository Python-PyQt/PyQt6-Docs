.. sip:method-description::
    :status: todo
    :pysig: 8737790c1f9f89e4183712ec1403ad97
    :realsig: (QCategory3DAxis*)
    :digest: 42e3c4422f3eb649bd68ddb463a73a00

Sets the axis of the active row to *axis*. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addAxis` to transfer the ownership of the axis to this graph.

If *axis* is null, a temporary default axis with no labels is created. This temporary axis is destroyed if another axis is set explicitly to the same orientation.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.rowAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.releaseAxis`.
