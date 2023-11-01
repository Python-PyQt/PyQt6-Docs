:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLShaderProgram
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtOpenGL/QOpenGLShaderProgram-c.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtOpenGL/QOpenGLShaderProgram-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceCode
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addCacheableShaderFromSourceCode-f-4.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceCode
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            Optional[str]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addCacheableShaderFromSourceCode-f-5.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceFile
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            Optional[str]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addCacheableShaderFromSourceFile-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addShader
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader`
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addShader-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addShaderFromSourceCode-f-4.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceCode
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            Optional[str]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addShaderFromSourceCode-f-5.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.addShaderFromSourceFile
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader.ShaderTypeBit`
            Optional[str]
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-addShaderFromSourceFile-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.attributeLocation
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-attributeLocation-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.attributeLocation
        :args:
            Optional[str]
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-attributeLocation-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.bind
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-bind-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.bindAttributeLocation
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            int
        :description: QtOpenGL/QOpenGLShaderProgram-bindAttributeLocation-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.bindAttributeLocation
        :args:
            Optional[str]
            int
        :description: QtOpenGL/QOpenGLShaderProgram-bindAttributeLocation-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.create
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-create-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.defaultInnerTessellationLevels
        :returns:
            List[float]
        :description: QtOpenGL/QOpenGLShaderProgram-defaultInnerTessellationLevels-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.defaultOuterTessellationLevels
        :returns:
            List[float]
        :description: QtOpenGL/QOpenGLShaderProgram-defaultOuterTessellationLevels-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.disableAttributeArray
        :args:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-disableAttributeArray-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.disableAttributeArray
        :args:
            str
        :description: QtOpenGL/QOpenGLShaderProgram-disableAttributeArray-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.enableAttributeArray
        :args:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-enableAttributeArray-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.enableAttributeArray
        :args:
            str
        :description: QtOpenGL/QOpenGLShaderProgram-enableAttributeArray-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.hasOpenGLShaderPrograms
        :args:
            context: :sip:ref:`~PyQt6.QtGui.QOpenGLContext` = None
        :returns:
            bool
        :static:
        :description: QtOpenGL/QOpenGLShaderProgram-hasOpenGLShaderPrograms-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.isLinked
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-isLinked-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.link
        :returns:
            bool
        :description: QtOpenGL/QOpenGLShaderProgram-link-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.log
        :returns:
            str
        :description: QtOpenGL/QOpenGLShaderProgram-log-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.maxGeometryOutputVertices
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-maxGeometryOutputVertices-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.patchVertexCount
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-patchVertexCount-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.programId
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-programId-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.release
        :description: QtOpenGL/QOpenGLShaderProgram-release-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.removeAllShaders
        :description: QtOpenGL/QOpenGLShaderProgram-removeAllShaders-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.removeShader
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader`
        :description: QtOpenGL/QOpenGLShaderProgram-removeShader-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeArray
        :args:
            int
            PYQT_SHADER_ATTRIBUTE_ARRAY
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeArray-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeArray
        :args:
            str
            PYQT_SHADER_ATTRIBUTE_ARRAY
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeArray-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeBuffer
        :args:
            int
            int
            int
            int
            stride: int = 0
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeBuffer-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeBuffer
        :args:
            str
            int
            int
            int
            stride: int = 0
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeBuffer-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QVector2D`
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QVector4D`
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-16.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-5.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QVector2D`
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-6.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-7.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QVector4D`
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-8.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-17.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-10.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-11.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-12.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-13.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            int
            float
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-14.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setAttributeValue
        :args:
            str
            float
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setAttributeValue-f-15.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setDefaultInnerTessellationLevels
        :args:
            Iterable[float]
        :description: QtOpenGL/QOpenGLShaderProgram-setDefaultInnerTessellationLevels-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setDefaultOuterTessellationLevels
        :args:
            Iterable[float]
        :description: QtOpenGL/QOpenGLShaderProgram-setDefaultOuterTessellationLevels-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setPatchVertexCount
        :args:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-setPatchVertexCount-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            int
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QVector2D`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QVector4D`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-4.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-46.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-6.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-7.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-8.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-9.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix2x2`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-10.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix2x3`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-11.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix2x4`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-12.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix3x2`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-13.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix3x3`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-14.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix3x4`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-15.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix4x2`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-16.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix4x3`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-17.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-18.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-19.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            int
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-20.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-21.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QVector2D`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-22.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-23.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QVector4D`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-24.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-47.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-26.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-27.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-28.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-29.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix2x2`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-30.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix2x3`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-31.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix2x4`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-32.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix3x2`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-33.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix3x3`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-34.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix3x4`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-35.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix4x2`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-36.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix4x3`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-37.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-38.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-39.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-40.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-41.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-42.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-43.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            int
            float
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-44.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValue
        :args:
            str
            float
            float
            float
            float
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValue-f-45.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValueArray
        :args:
            int
            PYQT_SHADER_UNIFORM_VALUE_ARRAY
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValueArray-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.setUniformValueArray
        :args:
            str
            PYQT_SHADER_UNIFORM_VALUE_ARRAY
        :description: QtOpenGL/QOpenGLShaderProgram-setUniformValueArray-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.shaders
        :returns:
            List[:sip:ref:`~PyQt6.QtOpenGL.QOpenGLShader`]
        :description: QtOpenGL/QOpenGLShaderProgram-shaders-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.uniformLocation
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-uniformLocation-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLShaderProgram.uniformLocation
        :args:
            Optional[str]
        :returns:
            int
        :description: QtOpenGL/QOpenGLShaderProgram-uniformLocation-f-3.rst
