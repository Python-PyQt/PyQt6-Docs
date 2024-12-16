.. sip:method-description::
    :status: todo
    :pysig: 90c538e7092ad7218301099f5636778a
    :realsig: (const QPoint&) const
    :digest: f905c956a71c479aa69e51ddc8d73963

Returns the viewport coordinate *point* mapped to scene coordinates.

Note: It can be useful to map the whole rectangle covered by the pixel at *point* instead of the point itself. To do this, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene`\ (\ :sip:ref:`~PyQt6.QtCore.QRect`\ (\ *point*, :sip:ref:`~PyQt6.QtCore.QSize`\ (2, 2))).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapFromScene`.
