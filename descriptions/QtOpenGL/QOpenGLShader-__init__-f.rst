.. sip:method-description::
    :status: todo
    :pysig: 5a856e10b9090b50c62acbe4cae54dea
    :realsig: (QOpenGLShader::ShaderType,QObject*)
    :digest: a1966a5d084833342293c2dd8b310834

Constructs a new :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader` object of the specified *type* and attaches it to *parent*. If shader programs are not supported, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.hasOpenGLShaderPrograms` will return false.

This constructor is normally followed by a call to :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.compileSourceCode` or :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.compileSourceFile`.

The shader will be associated with the current `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_.

.. seealso:: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.compileSourceCode`, :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.compileSourceFile`.
