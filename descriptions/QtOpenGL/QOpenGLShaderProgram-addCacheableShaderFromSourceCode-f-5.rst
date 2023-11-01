.. sip:method-description::
    :status: todo
    :pysig: 8bb6c4adadcec402be77aa13409dd6c3
    :realsig: (QOpenGLShader::ShaderType, const QString&)
    :digest: 7e9497b0d13bc7cb56f73df2522f9ffa

This is an overloaded function.

Registers the shader of the specified *type* and *source* to this program. Unlike :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`, this function does not perform compilation. Compilation is deferred to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, and may not happen at all, because :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link` may potentially use a program binary from Qt's shader disk cache. This will typically lead to a significant increase in performance.

When the disk cache is disabled, via :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DisableShaderDiskCache` for example, or the OpenGL context has no support for context binaries, calling this function is equivalent to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceFile`.
