.. sip:method-description::
    :status: todo
    :pysig: eefd9d8460abba002a7c7ef020a0ba84
    :realsig: (QOpenGLShader::ShaderType,const QByteArray&)
    :digest: 0487a0c80a750eb76bb8d499cb86566e

This is an overloaded function.

Registers the shader of the specified *type* and *source* to this program. Unlike :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`, this function does not perform compilation. Compilation is deferred to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link`, and may not happen at all, because :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.link` may potentially use a program binary from Qt's shader disk cache. This will typically lead to a significant increase in performance.

Returns true if the shader has been registered or, in the non-cached case, compiled successfully; false if there was an error. The compilation error messages can be retrieved via :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.log`.

When the disk cache is disabled, via :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DisableShaderDiskCache` for example, or the OpenGL context has no support for context binaries, calling this function is equivalent to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceFile`.
