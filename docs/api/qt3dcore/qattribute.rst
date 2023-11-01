:orphan:

.. sip:class:: PyQt6.Qt3DCore.QAttribute
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QNode`
    :description: Qt3DCore/QAttribute-c.rst

    .. sip:enum:: PyQt6.Qt3DCore.QAttribute.AttributeType
        :description: Qt3DCore/QAttribute-AttributeType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.AttributeType.DrawIndirectAttribute
            :description: Qt3DCore/QAttribute-AttributeType-DrawIndirectAttribute-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.AttributeType.IndexAttribute
            :description: Qt3DCore/QAttribute-AttributeType-IndexAttribute-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.AttributeType.VertexAttribute
            :description: Qt3DCore/QAttribute-AttributeType-VertexAttribute-v.rst

    .. sip:enum:: PyQt6.Qt3DCore.QAttribute.VertexBaseType
        :description: Qt3DCore/QAttribute-VertexBaseType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.Byte
            :description: Qt3DCore/QAttribute-VertexBaseType-Byte-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.Double
            :description: Qt3DCore/QAttribute-VertexBaseType-Double-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.Float
            :description: Qt3DCore/QAttribute-VertexBaseType-Float-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.HalfFloat
            :description: Qt3DCore/QAttribute-VertexBaseType-HalfFloat-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.Int
            :description: Qt3DCore/QAttribute-VertexBaseType-Int-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.Short
            :description: Qt3DCore/QAttribute-VertexBaseType-Short-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.UnsignedByte
            :description: Qt3DCore/QAttribute-VertexBaseType-UnsignedByte-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.UnsignedInt
            :description: Qt3DCore/QAttribute-VertexBaseType-UnsignedInt-v.rst

        .. sip:enum-member:: PyQt6.Qt3DCore.QAttribute.VertexBaseType.UnsignedShort
            :description: Qt3DCore/QAttribute-VertexBaseType-UnsignedShort-v.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QAttribute-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.__init__
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer`
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.VertexBaseType`
            int
            int
            offset: int = 0
            stride: int = 0
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QAttribute-__init__-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.__init__
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer`
            Optional[str]
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.VertexBaseType`
            int
            int
            offset: int = 0
            stride: int = 0
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QAttribute-__init__-f-3.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.attributeType
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.AttributeType`
        :description: Qt3DCore/QAttribute-attributeType-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.buffer
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer`
        :description: Qt3DCore/QAttribute-buffer-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.byteOffset
        :returns:
            int
        :description: Qt3DCore/QAttribute-byteOffset-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.byteStride
        :returns:
            int
        :description: Qt3DCore/QAttribute-byteStride-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.count
        :returns:
            int
        :description: Qt3DCore/QAttribute-count-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultColorAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultColorAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultJointIndicesAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultJointIndicesAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultJointWeightsAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultJointWeightsAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultNormalAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultNormalAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultPositionAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultPositionAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultTangentAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultTangentAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultTextureCoordinate1AttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultTextureCoordinate1AttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultTextureCoordinate2AttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultTextureCoordinate2AttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.defaultTextureCoordinateAttributeName
        :returns:
            str
        :static:
        :description: Qt3DCore/QAttribute-defaultTextureCoordinateAttributeName-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.divisor
        :returns:
            int
        :description: Qt3DCore/QAttribute-divisor-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.name
        :returns:
            str
        :description: Qt3DCore/QAttribute-name-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setAttributeType
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.AttributeType`
        :description: Qt3DCore/QAttribute-setAttributeType-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setBuffer
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer`
        :description: Qt3DCore/QAttribute-setBuffer-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setByteOffset
        :args:
            int
        :description: Qt3DCore/QAttribute-setByteOffset-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setByteStride
        :args:
            int
        :description: Qt3DCore/QAttribute-setByteStride-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setCount
        :args:
            int
        :description: Qt3DCore/QAttribute-setCount-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setDivisor
        :args:
            int
        :description: Qt3DCore/QAttribute-setDivisor-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setName
        :args:
            Optional[str]
        :description: Qt3DCore/QAttribute-setName-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setVertexBaseType
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.VertexBaseType`
        :description: Qt3DCore/QAttribute-setVertexBaseType-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.setVertexSize
        :args:
            int
        :description: Qt3DCore/QAttribute-setVertexSize-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.vertexBaseType
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.VertexBaseType`
        :description: Qt3DCore/QAttribute-vertexBaseType-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QAttribute.vertexSize
        :returns:
            int
        :description: Qt3DCore/QAttribute-vertexSize-f.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.attributeTypeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.AttributeType`
        :description: Qt3DCore/QAttribute-attributeTypeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.bufferChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QBuffer`
        :description: Qt3DCore/QAttribute-bufferChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.byteOffsetChanged
        :args:
            int
        :description: Qt3DCore/QAttribute-byteOffsetChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.byteStrideChanged
        :args:
            int
        :description: Qt3DCore/QAttribute-byteStrideChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.countChanged
        :args:
            int
        :description: Qt3DCore/QAttribute-countChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.dataSizeChanged
        :args:
            int
        :description: Qt3DCore/QAttribute-dataSizeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.dataTypeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.VertexBaseType`
        :description: Qt3DCore/QAttribute-dataTypeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.divisorChanged
        :args:
            int
        :description: Qt3DCore/QAttribute-divisorChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.nameChanged
        :args:
            Optional[str]
        :description: Qt3DCore/QAttribute-nameChanged-s-1.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.vertexBaseTypeChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DCore.QAttribute.VertexBaseType`
        :description: Qt3DCore/QAttribute-vertexBaseTypeChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QAttribute.vertexSizeChanged
        :args:
            int
        :description: Qt3DCore/QAttribute-vertexSizeChanged-s.rst
