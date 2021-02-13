.. sip:method-description::
    :status: todo
    :pysig: 9b698fc8cd273360d649d7d4005cb9c8
    :realsig: (float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float)
    :digest: d7a513056f68441acd9e08e828e5d980

Constructs a matrix from the 16 elements *m11*, *m12*, *m13*, *m14*, *m21*, *m22*, *m23*, *m24*, *m31*, *m32*, *m33*, *m34*, *m41*, *m42*, *m43*, and *m44*. The elements are specified in row-major order.

If the matrix has a special type (identity, translate, scale, etc), the programmer should follow this constructor with a call to :sip:ref:`~PyQt6.QtGui.QMatrix4x4.optimize` if they wish :sip:ref:`~PyQt6.QtGui.QMatrix4x4` to optimize further calls to :sip:ref:`~PyQt6.QtGui.QMatrix4x4.translate`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.scale`, etc.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.optimize`.
