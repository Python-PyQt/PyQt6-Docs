.. sip:method-description::
    :status: todo
    :pysig: d69eee048a0b0f57d29acd6afa97419d
    :realsig: (QOpenGLBuffer::Type)
    :digest: 1dc218c3796c15707f62c9edc4966b1a

Releases the buffer associated with *type* in the current `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_.

This function is a direct call to ``glBindBuffer(type, 0)`` for use when the caller does not know which :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer` has been bound to the context but wants to make sure that it is released.

.. literalinclude:: ../../../snippets/qtbase-src-opengl-doc-snippets-code-src_gui_opengl_qopenglbuffer.py
    :lines: 66-66
