.. sip:method-description::
    :status: todo
    :pysig: 8737790c1f9f89e4183712ec1403ad97
    :realsig: (QCategory3DAxis*)
    :digest: 3889407997e08b15e2e32d82077f6e1d

Sets the axis of the active column to *axis*. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addAxis` to transfer the ownership of the axis to this graph.

If *axis* is null, a temporary default axis with no labels is created. This temporary axis is destroyed if another axis is set explicitly to the same orientation.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.columnAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addAxis`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.releaseAxis`.
