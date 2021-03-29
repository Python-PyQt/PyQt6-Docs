.. sip:method-description::
    :status: todo
    :pysig: 2f451bad570b08b7f0c084061fb325ba
    :realsig: () const
    :digest: 9eeefd2980ea7cad94b0cffc0aac26a5

Creates a rotation matrix that corresponds to this quaternion.

**Note:** If this quaternion is not normalized, the resulting rotation matrix will contain scaling information.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.fromRotationMatrix`, :sip:ref:`~PyQt6.QtGui.QQuaternion.getAxes`.
