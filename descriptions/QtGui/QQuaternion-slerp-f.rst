.. sip:method-description::
    :status: todo
    :pysig: 2dcb126fec113aedee3cd8b325685a65
    :realsig: (const QQuaternion&,const QQuaternion&,float)
    :digest: 00f2a7fe16fb480862bd45df5217ad55

Interpolates along the shortest spherical path between the rotational positions *q1* and *q2*. The value *t* should be between 0 and 1, indicating the spherical distance to travel between *q1* and *q2*.

If *t* is less than or equal to 0, then *q1* will be returned. If *t* is greater than or equal to 1, then *q2* will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.nlerp`.
