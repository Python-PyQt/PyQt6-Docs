.. sip:method-description::
    :status: todo
    :pysig: 06efdb9e1abbfe481534ee21ace58fb7
    :realsig: (const QMatrix3x3&)
    :digest: c843dba76f7b6b60acf01149e023c23c

Creates a quaternion that corresponds to a rotation matrix *rot3x3*.

**Note:** If a given rotation matrix is not normalized, the resulting quaternion will contain scaling information.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.toRotationMatrix`, :sip:ref:`~PyQt6.QtGui.QQuaternion.fromAxes`.
