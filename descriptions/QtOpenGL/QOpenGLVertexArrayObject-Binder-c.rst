.. sip:class-description::
    :status: todo
    :brief: QOpenGLVertexArrayObject::Binder class is a convenience class to help with the binding and releasing of OpenGL Vertex Array Objects
    :digest: 5fc8c16d4468bee769ef64df1a8b0bd8

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.Binder` class is a convenience class to help with the binding and releasing of OpenGL Vertex Array Objects.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.Binder` is a simple convenience class that can be used to assist with the binding and releasing of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject` instances. This class is to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject` as QMutexLocker is to :sip:ref:`~PyQt6.QtCore.QMutex`.

This class implements the RAII principle which helps to ensure behavior in complex code or in the presence of exceptions.

The constructor of this class accepts a :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject` (VAO) as an argument and attempts to bind the VAO, calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.create` if necessary. The destructor of this class calls :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.release` which unbinds the VAO.

If needed the VAO can be temporarily unbound with the :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.Binder.release` function and bound once more with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.Binder.rebind`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject`.
