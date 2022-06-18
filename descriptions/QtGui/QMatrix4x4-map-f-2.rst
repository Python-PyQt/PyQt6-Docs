.. sip:method-description::
    :status: todo
    :pysig: 024ca1d0f36fb454057d1106e33fd7b9
    :realsig: (const QVector3D&) const
    :digest: 9823feb09eebdfd36f971b54afa736fc

Maps *point* by multiplying this matrix by *point* extended to a 4D vector by assuming 1.0 for the w coordinate. The matrix is applied pre-point.

**Note:** This function is not the same as :sip:ref:`~PyQt6.QtGui.QMatrix4x4.mapVector`. For points, always use :sip:ref:`~PyQt6.QtGui.QMatrix4x4.map`. :sip:ref:`~PyQt6.QtGui.QMatrix4x4.mapVector` is suitable for vectors (directions) only.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.mapRect`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.mapVector`.
