:orphan:

.. sip:class:: PyQt6.QtQuick.QSGGeometry
    :description: QtQuick/QSGGeometry-c.rst

    .. sip:enum:: PyQt6.QtQuick.QSGGeometry.AttributeType
        :description: QtQuick/QSGGeometry-AttributeType-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.AttributeType.ColorAttribute
            :description: QtQuick/QSGGeometry-AttributeType-ColorAttribute-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.AttributeType.PositionAttribute
            :description: QtQuick/QSGGeometry-AttributeType-PositionAttribute-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.AttributeType.TexCoord1Attribute
            :description: QtQuick/QSGGeometry-AttributeType-TexCoord1Attribute-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.AttributeType.TexCoord2Attribute
            :description: QtQuick/QSGGeometry-AttributeType-TexCoord2Attribute-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.AttributeType.TexCoordAttribute
            :description: QtQuick/QSGGeometry-AttributeType-TexCoordAttribute-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.AttributeType.UnknownAttribute
            :description: QtQuick/QSGGeometry-AttributeType-UnknownAttribute-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGGeometry.DataPattern
        :description: QtQuick/QSGGeometry-DataPattern-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DataPattern.AlwaysUploadPattern
            :description: QtQuick/QSGGeometry-DataPattern-AlwaysUploadPattern-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DataPattern.DynamicPattern
            :description: QtQuick/QSGGeometry-DataPattern-DynamicPattern-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DataPattern.StaticPattern
            :description: QtQuick/QSGGeometry-DataPattern-StaticPattern-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DataPattern.StreamPattern
            :description: QtQuick/QSGGeometry-DataPattern-StreamPattern-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGGeometry.DrawingMode
        :description: QtQuick/QSGGeometry-DrawingMode-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLineLoop
            :description: QtQuick/QSGGeometry-DrawingMode-DrawLineLoop-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLines
            :description: QtQuick/QSGGeometry-DrawingMode-DrawLines-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLineStrip
            :description: QtQuick/QSGGeometry-DrawingMode-DrawLineStrip-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawPoints
            :description: QtQuick/QSGGeometry-DrawingMode-DrawPoints-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawTriangleFan
            :description: QtQuick/QSGGeometry-DrawingMode-DrawTriangleFan-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawTriangles
            :description: QtQuick/QSGGeometry-DrawingMode-DrawTriangles-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawTriangleStrip
            :description: QtQuick/QSGGeometry-DrawingMode-DrawTriangleStrip-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGGeometry.Type
        :description: QtQuick/QSGGeometry-Type-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.Bytes2Type
            :description: QtQuick/QSGGeometry-Type-Bytes2Type-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.Bytes3Type
            :description: QtQuick/QSGGeometry-Type-Bytes3Type-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.Bytes4Type
            :description: QtQuick/QSGGeometry-Type-Bytes4Type-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.ByteType
            :description: QtQuick/QSGGeometry-Type-ByteType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.DoubleType
            :description: QtQuick/QSGGeometry-Type-DoubleType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.FloatType
            :description: QtQuick/QSGGeometry-Type-FloatType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.IntType
            :description: QtQuick/QSGGeometry-Type-IntType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.ShortType
            :description: QtQuick/QSGGeometry-Type-ShortType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.UnsignedByteType
            :description: QtQuick/QSGGeometry-Type-UnsignedByteType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.UnsignedIntType
            :description: QtQuick/QSGGeometry-Type-UnsignedIntType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGGeometry.Type.UnsignedShortType
            :description: QtQuick/QSGGeometry-Type-UnsignedShortType-v.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.__init__
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.AttributeSet`
            int
            indexCount: int = 0
            indexType: int = :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.UnsignedShortType`
        :description: QtQuick/QSGGeometry-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.allocate
        :args:
            int
            indexCount: int = 0
        :description: QtQuick/QSGGeometry-allocate-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.attributeCount
        :returns:
            int
        :description: QtQuick/QSGGeometry-attributeCount-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.attributes
        :returns:
            PyQt6.sip.array[QSGGeometry.Attribute]
        :description: QtQuick/QSGGeometry-attributes-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.defaultAttributes_ColoredPoint2D
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.AttributeSet`
        :static:
        :description: QtQuick/QSGGeometry-defaultAttributes_ColoredPoint2D-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.defaultAttributes_Point2D
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.AttributeSet`
        :static:
        :description: QtQuick/QSGGeometry-defaultAttributes_Point2D-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.defaultAttributes_TexturedPoint2D
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.AttributeSet`
        :static:
        :description: QtQuick/QSGGeometry-defaultAttributes_TexturedPoint2D-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.drawingMode
        :returns:
            int
        :description: QtQuick/QSGGeometry-drawingMode-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.indexCount
        :returns:
            int
        :description: QtQuick/QSGGeometry-indexCount-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.indexData
        :returns:
            sip.voidptr
        :description: QtQuick/QSGGeometry-indexData-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.indexDataAsUInt
        :returns:
            PyQt6.sip.array[int]
        :description: QtQuick/QSGGeometry-indexDataAsUInt-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.indexDataAsUShort
        :returns:
            PyQt6.sip.array[int]
        :description: QtQuick/QSGGeometry-indexDataAsUShort-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.indexDataPattern
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DataPattern`
        :description: QtQuick/QSGGeometry-indexDataPattern-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.indexType
        :returns:
            int
        :description: QtQuick/QSGGeometry-indexType-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.lineWidth
        :returns:
            float
        :description: QtQuick/QSGGeometry-lineWidth-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.markIndexDataDirty
        :description: QtQuick/QSGGeometry-markIndexDataDirty-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.markVertexDataDirty
        :description: QtQuick/QSGGeometry-markVertexDataDirty-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.setDrawingMode
        :args:
            int
        :description: QtQuick/QSGGeometry-setDrawingMode-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.setIndexDataPattern
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DataPattern`
        :description: QtQuick/QSGGeometry-setIndexDataPattern-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.setLineWidth
        :args:
            float
        :description: QtQuick/QSGGeometry-setLineWidth-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.setVertexDataPattern
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DataPattern`
        :description: QtQuick/QSGGeometry-setVertexDataPattern-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.sizeOfIndex
        :returns:
            int
        :description: QtQuick/QSGGeometry-sizeOfIndex-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.sizeOfVertex
        :returns:
            int
        :description: QtQuick/QSGGeometry-sizeOfVertex-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.updateColoredRectGeometry
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry`
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :static:
        :description: QtQuick/QSGGeometry-updateColoredRectGeometry-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.updateRectGeometry
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry`
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :static:
        :description: QtQuick/QSGGeometry-updateRectGeometry-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.updateTexturedRectGeometry
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry`
            :sip:ref:`~PyQt6.QtCore.QRectF`
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :static:
        :description: QtQuick/QSGGeometry-updateTexturedRectGeometry-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.vertexCount
        :returns:
            int
        :description: QtQuick/QSGGeometry-vertexCount-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.vertexData
        :returns:
            sip.voidptr
        :description: QtQuick/QSGGeometry-vertexData-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.vertexDataAsColoredPoint2D
        :returns:
            PyQt6.sip.array[QSGGeometry.ColoredPoint2D]
        :description: QtQuick/QSGGeometry-vertexDataAsColoredPoint2D-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.vertexDataAsPoint2D
        :returns:
            PyQt6.sip.array[QSGGeometry.Point2D]
        :description: QtQuick/QSGGeometry-vertexDataAsPoint2D-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.vertexDataAsTexturedPoint2D
        :returns:
            PyQt6.sip.array[QSGGeometry.TexturedPoint2D]
        :description: QtQuick/QSGGeometry-vertexDataAsTexturedPoint2D-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGGeometry.vertexDataPattern
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DataPattern`
        :description: QtQuick/QSGGeometry-vertexDataPattern-f.rst
