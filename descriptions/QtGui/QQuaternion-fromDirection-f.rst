.. sip:method-description::
    :status: todo
    :pysig: db87e2300778c307b8f43a77411224bf
    :realsig: (const QVector3D&,const QVector3D&)
    :digest: 6c3f5e64d6511702f7f63195e834feb4

Constructs the quaternion using specified forward direction *direction* and upward direction *up*. If the upward direction was not specified or the forward and upward vectors are collinear, a new orthonormal upward direction will be generated.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.fromAxes`, :sip:ref:`~PyQt6.QtGui.QQuaternion.rotationTo`.
