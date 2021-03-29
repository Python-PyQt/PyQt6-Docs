.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: f83a1dfcd55b72489fbf0cc7805f2460

Creates the underlying OpenGL vertex array object. There must be a valid OpenGL context that supports vertex array objects current for this function to succeed.

Returns ``true`` if the OpenGL vertex array object was successfully created.

When the return value is ``false``, vertex array object support is not available. This is not an error: on systems with OpenGL 2.x or OpenGL ES 2.0 vertex array objects may not be supported. The application is free to continue execution in this case, but it then has to be prepared to operate in a VAO-less manner too. This means that instead of merely calling :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.bind`, the value of :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.isCreated` must be checked and the vertex arrays has to be initialized in the traditional way when there is no vertex array object present.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLVertexArrayObject.isCreated`.
