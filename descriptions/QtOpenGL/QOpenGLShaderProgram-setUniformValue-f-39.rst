.. sip:method-description::
    :status: todo
    :pysig: 4d87a83bb4e3720149b16a24d18592a4
    :realsig: (const char*,const QTransform&)
    :digest: d9c148dad3ee4366dfd685ef52ecbd26

Sets the uniform variable called *name* in the current context to a 3x3 transformation matrix *value* that is specified as a :sip:ref:`~PyQt6.QtGui.QTransform` value.

To set a :sip:ref:`~PyQt6.QtGui.QTransform` value as a 4x4 matrix in a shader, use ``setUniformValue(name, QMatrix4x4(value))``.
