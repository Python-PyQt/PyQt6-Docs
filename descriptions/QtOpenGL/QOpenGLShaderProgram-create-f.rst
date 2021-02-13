.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: b6fe91f02baae681fb1d1604ce91df48

Requests the shader program's id to be created immediately. Returns ``true`` if successful; ``false`` otherwise.

This function is primarily useful when combining :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` with other OpenGL functions that operate directly on the shader program id, like ``GL_OES_get_program_binary``.

When the shader program is used normally, the shader program's id will be created on demand.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.programId`.
