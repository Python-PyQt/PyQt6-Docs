.. sip:method-description::
    :status: todo
    :pysig: eed5c663a9110c04fdce085b268c2b9d
    :realsig: (float*,float*,float*) const
    :digest: 435696c21fb1b8093aab4475d1a5c957

Calculates *roll*, *pitch*, and *yaw* Euler angles (in degrees) that corresponds to this quaternion.

All of *pitch*, *yaw*, and *roll* must be valid, non-``nullptr`` pointers, otherwise the behavior is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.fromEulerAngles`.
