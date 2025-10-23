.. sip:method-description::
    :status: todo
    :pysig: 06efdb9e1abbfe481534ee21ace58fb7
    :realsig: (const QMatrix3x3&)
    :digest: 75a7ea4059fe9615e5092beeac4ba1c1

Creates a quaternion that corresponds to the rotation matrix *rot3x3*.

**Note:** If the given rotation matrix is not normalized, the resulting quaternion will contain scaling information.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.toRotationMatrix`, :sip:ref:`~PyQt6.QtGui.QQuaternion.fromAxes`.
