.. sip:method-description::
    :status: todo
    :pysig: 8e31615fab591ba16ef8439d108377a8
    :realsig: (QOpenGLShader*)
    :digest: 22b4da44522613879366a1c04954840c

Adds a compiled *shader* to this shader program. Returns ``true`` if the shader could be added, or false otherwise.

Ownership of the *shader* object remains with the caller. It will not be deleted when this :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram` instance is deleted. This allows the caller to add the same shader to multiple shader programs.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.removeShader`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.removeAllShaders`.
