.. sip:class-description::
    :status: todo
    :brief: Represents a 4x4 transformation matrix in 3D space
    :digest: e5e321c46999fcda0aef94a8ed113c9f

The :sip:ref:`~PyQt6.QtGui.QMatrix4x4` class represents a 4x4 transformation matrix in 3D space.

The :sip:ref:`~PyQt6.QtGui.QMatrix4x4` class in general is treated as a row-major matrix, in that the constructors and operator() functions take data in row-major format, as is familiar in C-style usage.

Internally the data is stored as column-major format, so as to be optimal for passing to OpenGL functions, which expect column-major data.

When using these functions be aware that they return data in **column-major** format:

* :sip:ref:`~PyQt6.QtGui.QMatrix4x4.data`

* constData()

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVector3D`, QGenericMatrix.
