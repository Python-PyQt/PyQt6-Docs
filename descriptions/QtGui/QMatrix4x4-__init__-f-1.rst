.. sip:method-description::
    :status: todo
    :pysig: e21385c364c155728fc8341125676e72
    :realsig: (const float*)
    :digest: 039352a1df9f5700b22c86fc87298778

Constructs a matrix from the given 16 floating-point *values*. The contents of the array *values* is assumed to be in row-major order.

If the matrix has a special type (identity, translate, scale, etc), the programmer should follow this constructor with a call to :sip:ref:`~PyQt6.QtGui.QMatrix4x4.optimize` if they wish :sip:ref:`~PyQt6.QtGui.QMatrix4x4` to optimize further calls to :sip:ref:`~PyQt6.QtGui.QMatrix4x4.translate`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.scale`, etc.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.copyDataTo`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.optimize`.
