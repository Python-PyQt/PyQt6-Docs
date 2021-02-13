.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 46bcdf9a1e97e283b8eb617f9e4b3e3a

Unmaps the buffer after it was mapped into the application's memory space with a previous call to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.map`. Returns ``true`` if the unmap succeeded; false otherwise.

It is assumed that this buffer has been bound to the current context, and that it was previously mapped with :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.map`.

**Note:** This function is only supported under OpenGL ES 2.0 and earlier if the ``GL_OES_mapbuffer`` extension is present.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLBuffer.map`.
