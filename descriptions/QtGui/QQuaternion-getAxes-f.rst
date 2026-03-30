.. sip:method-description::
    :status: todo
    :pysig: 5f2ac4790b1e0502d2b5442b3b34d07f
    :realsig: (QVector3D*,QVector3D*,QVector3D*) const
    :digest: 37950bbe102561dd9e6e9d1fe249e5b0

Use :sip:ref:`~PyQt6.QtGui.QQuaternion.toAxes` instead.

Returns the 3 orthonormal axes (\ *xAxis*, *yAxis*, *zAxis*) defining the quaternion.

All of *xAxis*, *yAxis*, and *zAxis* must be valid, non-``nullptr`` pointers, otherwise the behavior is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.fromAxes`, :sip:ref:`~PyQt6.QtGui.QQuaternion.toRotationMatrix`.
