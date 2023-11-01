:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLShader
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtOpenGL/QOpenGLShader-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit
        :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit.Compute
            :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-Compute-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit.Fragment
            :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-Fragment-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit.Geometry
            :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-Geometry-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit.TessellationControl
            :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-TessellationControl-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit.TessellationEvaluation
            :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-TessellationEvaluation-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit.Vertex
            :description: QtOpenGL/QOpenGLShader-ShaderTypeBit-Vertex-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.__init__
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtOpenGL/QOpenGLShader-__init__-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.compileSourceCode
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-compileSourceCode-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.compileSourceCode
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-compileSourceCode-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.compileSourceFile
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-compileSourceFile-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.hasOpenGLShaders
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            context: :sip:ref:`~PyQt6.QtGui.QOpenGLContext` = None
        :returns:
            bool
        :static:
        :description: QtOpenGL/QOpenGLShader-hasOpenGLShaders-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.isCompiled
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-isCompiled-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.log
        :returns:
            str
        :description: QtOpenGL/QOpenGLShader-log-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.shaderId
        :returns:
            int
        :description: QtOpenGL/QOpenGLShader-shaderId-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.shaderType
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
        :description: QtOpenGL/QOpenGLShader-shaderType-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.sourceCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtOpenGL/QOpenGLShader-sourceCode-f.rst
