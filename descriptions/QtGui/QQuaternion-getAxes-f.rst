.. sip:method-description::
    :status: todo
    :pysig: 5f2ac4790b1e0502d2b5442b3b34d07f
    :realsig: (QVector3D*,QVector3D*,QVector3D*) const
    :digest: ee44bd64ad7f5e95651205b6673ac56f

Returns the 3 orthonormal axes (\ *xAxis*, *yAxis*, *zAxis*) defining the quaternion.

All of *xAxis*, *yAxis*, and *zAxis* must be valid, non-``nullptr`` pointers, otherwise the behavior is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QQuaternion.fromAxes`, :sip:ref:`~PyQt6.QtGui.QQuaternion.toRotationMatrix`.
