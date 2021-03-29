.. sip:class-description::
    :status: todo
    :brief: Functions for creating and managing OpenGL buffer objects
    :digest: 3f1512820278fc9fc3165c0abd48a1ed

The :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer` class provides functions for creating and managing OpenGL buffer objects.

Buffer objects are created in the OpenGL server so that the client application can avoid uploading vertices, indices, texture image data, etc every time they are needed.

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer` objects can be copied around as a reference to the underlying OpenGL buffer object:

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopenglbuffer.py
    :lines: 58-61

:sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer` performs a shallow copy when objects are copied in this manner, but does not implement copy-on-write semantics. The original object will be affected whenever the copy is modified.
