.. sip:method-description::
    :status: todo
    :pysig: eed5c663a9110c04fdce085b268c2b9d
    :realsig: (float*,float*,float*) const
    :digest: b551b6d07d2b338b44a590e1b653509c

Use eulerAngles() instead.

Calculates *roll*, *pitch*, and *yaw* Euler angles (in degrees) that corresponds to this quaternion.

All of *pitch*, *yaw*, and *roll* must be valid, non-``nullptr`` pointers, otherwise the behavior is undefined.

.. seealso:: eulerAngles(), :sip:ref:`~PyQt6.QtGui.QQuaternion.fromEulerAngles`.
