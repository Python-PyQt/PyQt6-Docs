.. sip:method-description::
    :status: todo
    :pysig: 7479ae58b3c0efe0492ae7e9551ab592
    :realsig: (QOpenGLShader::ShaderType,const QString&)
    :digest: 79b4753a2272eb45b89b996b6af4ae7c

Registers the shader of the specified *type* and *fileName* to this program. Unlike :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile`, this function does not perform compilation. Compilation is deferred to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, and may not happen at all, because :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link` may potentially use a program binary from Qt's shader disk cache. This will typically lead to a significant increase in performance.

Returns true if the file has been read successfully, false if the file could not be opened or the normal, non-cached compilation of the shader has failed. The compilation error messages can be retrieved via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.

When the disk cache is disabled, via :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DisableShaderDiskCache` for example, or the OpenGL context has no support for context binaries, calling this function is equivalent to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceCode`.
