:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLShader
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtOpenGL/QOpenGLShader-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType
        :description: QtOpenGL/QOpenGLShader-ShaderType-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType.Compute
            :description: QtOpenGL/QOpenGLShader-ShaderType-Compute-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType.Fragment
            :description: QtOpenGL/QOpenGLShader-ShaderType-Fragment-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType.Geometry
            :description: QtOpenGL/QOpenGLShader-ShaderType-Geometry-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType.TessellationControl
            :description: QtOpenGL/QOpenGLShader-ShaderType-TessellationControl-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType.TessellationEvaluation
            :description: QtOpenGL/QOpenGLShader-ShaderType-TessellationEvaluation-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLShader.ShaderType.Vertex
            :description: QtOpenGL/QOpenGLShader-ShaderType-Vertex-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.__init__
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderType`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtOpenGL/QOpenGLShader-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.compileSourceCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-compileSourceCode-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.compileSourceCode
        :args:
            str
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-compileSourceCode-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.compileSourceFile
        :args:
            str
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShader-compileSourceFile-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.hasOpenGLShaders
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderType`
            context: :sip:ref:`~PyQt6.QtGui.QOpenGLContext` = None
        :returns:
            bool
        :static:
        :description: QtOpenGL/QOpenGLShader-hasOpenGLShaders-f.rst

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
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderType`
        :description: QtOpenGL/QOpenGLShader-shaderType-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShader.sourceCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtOpenGL/QOpenGLShader-sourceCode-f.rst
