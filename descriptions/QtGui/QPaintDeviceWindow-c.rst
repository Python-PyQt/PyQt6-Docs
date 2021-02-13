.. sip:class-description::
    :status: todo
    :brief: Convenience subclass of QWindow that is also a QPaintDevice
    :digest: d1501345a38a50c8344f502b261beaac

Convenience subclass of :sip:ref:`~PyQt6.QtGui.QWindow` that is also a :sip:ref:`~PyQt6.QtGui.QPaintDevice`.

:sip:ref:`~PyQt6.QtGui.QPaintDeviceWindow` is like a regular :sip:ref:`~PyQt6.QtGui.QWindow`, with the added functionality of being a paint device too. Whenever the content needs to be updated, the virtual :sip:ref:`~PyQt6.QtGui.QPaintDeviceWindow.paintEvent` function is called. Subclasses, that reimplement this function, can then simply open a :sip:ref:`~PyQt6.QtGui.QPainter` on the window.

**Note:** This class cannot directly be used in applications. It rather serves as a base for subclasses like QOpenGLWindow.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLWindow`.
