:orphan:

.. sip:class:: PyQt6.QtCore.QCborStreamReader
    :description: QtCore/QCborStreamReader-c.rst

    .. sip:enum:: PyQt6.QtCore.QCborStreamReader.StringResultCode
        :description: QtCore/QCborStreamReader-StringResultCode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.StringResultCode.EndOfString
            :description: QtCore/QCborStreamReader-StringResultCode-EndOfString-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.StringResultCode.Error
            :description: QtCore/QCborStreamReader-StringResultCode-Error-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.StringResultCode.Ok
            :description: QtCore/QCborStreamReader-StringResultCode-Ok-v.rst

    .. sip:enum:: PyQt6.QtCore.QCborStreamReader.Type
        :description: QtCore/QCborStreamReader-Type-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Array
            :description: QtCore/QCborStreamReader-Type-Array-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.ByteArray
            :description: QtCore/QCborStreamReader-Type-ByteArray-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.ByteString
            :description: QtCore/QCborStreamReader-Type-ByteString-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Double
            :description: QtCore/QCborStreamReader-Type-Double-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Float
            :description: QtCore/QCborStreamReader-Type-Float-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Float16
            :description: QtCore/QCborStreamReader-Type-Float16-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.HalfFloat
            :description: QtCore/QCborStreamReader-Type-HalfFloat-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Invalid
            :description: QtCore/QCborStreamReader-Type-Invalid-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Map
            :description: QtCore/QCborStreamReader-Type-Map-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.NegativeInteger
            :description: QtCore/QCborStreamReader-Type-NegativeInteger-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.SimpleType
            :description: QtCore/QCborStreamReader-Type-SimpleType-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.String
            :description: QtCore/QCborStreamReader-Type-String-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.Tag
            :description: QtCore/QCborStreamReader-Type-Tag-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.TextString
            :description: QtCore/QCborStreamReader-Type-TextString-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QCborStreamReader.Type.UnsignedInteger
            :description: QtCore/QCborStreamReader-Type-UnsignedInteger-v.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.__init__
        :description: QtCore/QCborStreamReader-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.__init__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QCborStreamReader-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QCborStreamReader-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.addData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QCborStreamReader-addData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.clear
        :description: QtCore/QCborStreamReader-clear-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.containerDepth
        :returns:
            int
        :description: QtCore/QCborStreamReader-containerDepth-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.currentOffset
        :returns:
            int
        :description: QtCore/QCborStreamReader-currentOffset-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QCborStreamReader-device-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.enterContainer
        :returns:
            bool
        :description: QtCore/QCborStreamReader-enterContainer-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.hasNext
        :returns:
            bool
        :description: QtCore/QCborStreamReader-hasNext-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isArray
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isArray-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isBool
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isBool-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isByteArray
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isByteArray-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isContainer
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isContainer-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isDouble
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isFalse
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isFalse-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isFloat
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isFloat-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isFloat16
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isFloat16-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isInteger
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isInteger-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isInvalid
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isInvalid-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isLengthKnown
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isLengthKnown-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isMap
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isMap-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isNegativeInteger
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isNegativeInteger-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isNull
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isNull-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isSimpleType
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isSimpleType-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isSimpleType
        :args:
            :sip:ref:`~PyQt6.QtCore.QCborSimpleType`
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isSimpleType-f-1.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isString
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isString-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isTag
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isTag-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isTrue
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isTrue-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isUndefined
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isUndefined-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isUnsignedInteger
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isUnsignedInteger-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.isValid
        :returns:
            bool
        :description: QtCore/QCborStreamReader-isValid-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.lastError
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCborError`
        :description: QtCore/QCborStreamReader-lastError-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.leaveContainer
        :returns:
            bool
        :description: QtCore/QCborStreamReader-leaveContainer-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.__len__
        :returns:
            int
        :description: QtCore/QCborStreamReader-__len__-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.length
        :returns:
            int
        :description: QtCore/QCborStreamReader-length-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.next
        :args:
            maxRecursion: int = 10000
        :returns:
            bool
        :description: QtCore/QCborStreamReader-next-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.parentContainerType
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type`
        :description: QtCore/QCborStreamReader-parentContainerType-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.readByteArray
        :returns:
            Tuple[:sip:ref:`~PyQt6.QtCore.QByteArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.StringResultCode`]
        :description: QtCore/QCborStreamReader-readByteArray-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.readString
        :returns:
            Tuple[str, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.StringResultCode`]
        :description: QtCore/QCborStreamReader-readString-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.reparse
        :description: QtCore/QCborStreamReader-reparse-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.reset
        :description: QtCore/QCborStreamReader-reset-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QCborStreamReader-setDevice-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.toBool
        :returns:
            bool
        :description: QtCore/QCborStreamReader-toBool-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.toDouble
        :returns:
            float
        :description: QtCore/QCborStreamReader-toDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.toInteger
        :returns:
            int
        :description: QtCore/QCborStreamReader-toInteger-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.toSimpleType
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCborSimpleType`
        :description: QtCore/QCborStreamReader-toSimpleType-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.toUnsignedInteger
        :returns:
            int
        :description: QtCore/QCborStreamReader-toUnsignedInteger-f.rst

    .. sip:method:: PyQt6.QtCore.QCborStreamReader.type
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type`
        :description: QtCore/QCborStreamReader-type-f.rst
