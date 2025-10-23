.. sip:method-description::
    :status: todo
    :pysig: 54b662052d3b43dc24d4d376eaf7b938
    :realsig: (QVector3D*,float*) const
    :digest: c96ed052b853fa6129e038db2d4f0500

Extracts a 3D axis *axis* and a rotating angle *angle* (in degrees) that corresponds to this quaternion.

Both *axis* and *angle* must be valid, non-``nullptr`` pointers, otherwise the behavior is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.fromAxisAndAngle`.
