.. sip:method-description::
    :status: todo
    :pysig: 2dcb126fec113aedee3cd8b325685a65
    :realsig: (const QQuaternion&,const QQuaternion&,float)
    :digest: dbb58035de35f2c248036c70088bf4d3

Interpolates along the shortest linear path between the rotational positions *q1* and *q2*. The value *t* should be between 0 and 1, indicating the distance to travel between *q1* and *q2*. The result will be :sip:ref:`~PyQt6.QtGui.QQuaternion.normalized`.

If *t* is less than or equal to 0, then *q1* will be returned. If *t* is greater than or equal to 1, then *q2* will be returned.

The nlerp() function is typically faster than :sip:ref:`~PyQt6.QtGui.QQuaternion.slerp` and will give approximate results to spherical interpolation that are good enough for some applications.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.slerp`.
