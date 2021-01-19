:orphan:

.. sip:class:: PyQt6.Qt3DRender.QShaderProgram
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QNode`
    :description: Qt3DRender/QShaderProgram-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QShaderProgram.Format
        :description: Qt3DRender/QShaderProgram-Format-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.Format.GLSL
            :description: Qt3DRender/QShaderProgram-Format-GLSL-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.Format.SPIRV
            :description: Qt3DRender/QShaderProgram-Format-SPIRV-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QShaderProgram.ShaderType
        :description: Qt3DRender/QShaderProgram-ShaderType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.ShaderType.Compute
            :description: Qt3DRender/QShaderProgram-ShaderType-Compute-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.ShaderType.Fragment
            :description: Qt3DRender/QShaderProgram-ShaderType-Fragment-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.ShaderType.Geometry
            :description: Qt3DRender/QShaderProgram-ShaderType-Geometry-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.ShaderType.TessellationControl
            :description: Qt3DRender/QShaderProgram-ShaderType-TessellationControl-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.ShaderType.TessellationEvaluation
            :description: Qt3DRender/QShaderProgram-ShaderType-TessellationEvaluation-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.ShaderType.Vertex
            :description: Qt3DRender/QShaderProgram-ShaderType-Vertex-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QShaderProgram.Status
        :description: Qt3DRender/QShaderProgram-Status-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.Status.Error
            :description: Qt3DRender/QShaderProgram-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.Status.NotReady
            :description: Qt3DRender/QShaderProgram-Status-NotReady-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QShaderProgram.Status.Ready
            :description: Qt3DRender/QShaderProgram-Status-Ready-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QShaderProgram-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.computeShaderCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-computeShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.format
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.Format`
        :description: Qt3DRender/QShaderProgram-format-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.fragmentShaderCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-fragmentShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.geometryShaderCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-geometryShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.loadSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: Qt3DRender/QShaderProgram-loadSource-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.log
        :returns:
            str
        :description: Qt3DRender/QShaderProgram-log-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setComputeShaderCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setComputeShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setFormat
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.Format`
        :description: Qt3DRender/QShaderProgram-setFormat-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setFragmentShaderCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setFragmentShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setGeometryShaderCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setGeometryShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setShaderCode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.ShaderType`
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setTessellationControlShaderCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setTessellationControlShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setTessellationEvaluationShaderCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setTessellationEvaluationShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.setVertexShaderCode
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-setVertexShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.shaderCode
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.ShaderType`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-shaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.status
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.Status`
        :description: Qt3DRender/QShaderProgram-status-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.tessellationControlShaderCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-tessellationControlShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.tessellationEvaluationShaderCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-tessellationEvaluationShaderCode-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QShaderProgram.vertexShaderCode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-vertexShaderCode-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.computeShaderCodeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-computeShaderCodeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.formatChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.Format`
        :description: Qt3DRender/QShaderProgram-formatChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.fragmentShaderCodeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-fragmentShaderCodeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.geometryShaderCodeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-geometryShaderCodeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.logChanged
        :args:
            str
        :description: Qt3DRender/QShaderProgram-logChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.statusChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QShaderProgram.Status`
        :description: Qt3DRender/QShaderProgram-statusChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.tessellationControlShaderCodeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-tessellationControlShaderCodeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.tessellationEvaluationShaderCodeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-tessellationEvaluationShaderCodeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QShaderProgram.vertexShaderCodeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: Qt3DRender/QShaderProgram-vertexShaderCodeChanged-s.rst
