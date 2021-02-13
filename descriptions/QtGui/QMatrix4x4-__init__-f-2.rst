.. sip:method-description::
    :status: todo
    :pysig: e27247e5b452ce98dcfc93f19679f890
    :realsig: (const QTransform&)
    :digest: 58eb7796b26984394ced5f7c8e22d5dd

Constructs a 4x4 matrix from the conventional Qt 2D transformation matrix *transform*.

If *transform* has a special type (identity, translate, scale, etc), the programmer should follow this constructor with a call to :sip:ref:`~PyQt6.QtGui.QMatrix4x4.optimize` if they wish :sip:ref:`~PyQt6.QtGui.QMatrix4x4` to optimize further calls to :sip:ref:`~PyQt6.QtGui.QMatrix4x4.translate`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.scale`, etc.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.toTransform`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.optimize`.
