:orphan:

.. sip:class:: PyQt6.QtCore.QJsonValue
    :description: QtCore/QJsonValue-c.rst

    .. sip:enum:: PyQt6.QtCore.QJsonValue.Type
        :description: QtCore/QJsonValue-Type-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.Array
            :description: QtCore/QJsonValue-Type-Array-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.Bool
            :description: QtCore/QJsonValue-Type-Bool-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.Double
            :description: QtCore/QJsonValue-Type-Double-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.Null
            :description: QtCore/QJsonValue-Type-Null-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.Object
            :description: QtCore/QJsonValue-Type-Object-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.String
            :description: QtCore/QJsonValue-Type-String-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonValue.Type.Undefined
            :description: QtCore/QJsonValue-Type-Undefined-v.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__init__
        :args:
            type: :sip:ref:`~PyQt6.QtCore.QJsonValue.Type` = :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.Null`
        :description: QtCore/QJsonValue-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None
        :description: QtCore/QJsonValue-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__eq__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None
        :returns:
            bool
        :description: QtCore/QJsonValue-__eq__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.fromJson
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`|bytes|bytearray|memoryview
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
            :sip:ref:`~PyQt6.QtCore.QJsonParseError`
        :static:
        :description: QtCore/QJsonValue-fromJson-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.fromVariant
        :args:
            Any
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :static:
        :description: QtCore/QJsonValue-fromVariant-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__getitem__
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :description: QtCore/QJsonValue-__getitem__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__getitem__
        :args:
            str|None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :description: QtCore/QJsonValue-__getitem__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__hash__
        :returns:
            int
        :description: QtCore/QJsonValue-__hash__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isArray
        :returns:
            bool
        :description: QtCore/QJsonValue-isArray-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isBool
        :returns:
            bool
        :description: QtCore/QJsonValue-isBool-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isDouble
        :returns:
            bool
        :description: QtCore/QJsonValue-isDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isNull
        :returns:
            bool
        :description: QtCore/QJsonValue-isNull-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isObject
        :returns:
            bool
        :description: QtCore/QJsonValue-isObject-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isString
        :returns:
            bool
        :description: QtCore/QJsonValue-isString-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.isUndefined
        :returns:
            bool
        :description: QtCore/QJsonValue-isUndefined-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.__ne__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None
        :returns:
            bool
        :description: QtCore/QJsonValue-__ne__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :description: QtCore/QJsonValue-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toArray
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QJsonValue`]
        :description: QtCore/QJsonValue-toArray-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toArray
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None]
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QJsonValue`]
        :description: QtCore/QJsonValue-toArray-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toBool
        :args:
            defaultValue: bool = False
        :returns:
            bool
        :description: QtCore/QJsonValue-toBool-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toDouble
        :args:
            defaultValue: float = 0
        :returns:
            float
        :description: QtCore/QJsonValue-toDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toInt
        :args:
            defaultValue: int = 0
        :returns:
            int
        :description: QtCore/QJsonValue-toInt-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toInteger
        :args:
            defaultValue: int = 0
        :returns:
            int
        :description: QtCore/QJsonValue-toInteger-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toJson
        :args:
            format: :sip:ref:`~PyQt6.QtCore.QJsonDocument.JsonFormat` = :sip:ref:`~PyQt6.QtCore.QJsonDocument.JsonFormat.Indented`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QJsonValue-toJson-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toObject
        :returns:
            dict[str, :sip:ref:`~PyQt6.QtCore.QJsonValue`]
        :description: QtCore/QJsonValue-toObject-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toObject
        :args:
            dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None]
        :returns:
            dict[str, :sip:ref:`~PyQt6.QtCore.QJsonValue`]
        :description: QtCore/QJsonValue-toObject-f-2.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toString
        :returns:
            str
        :description: QtCore/QJsonValue-toString-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toString
        :args:
            str|None
        :returns:
            str
        :description: QtCore/QJsonValue-toString-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.toVariant
        :returns:
            Any
        :description: QtCore/QJsonValue-toVariant-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonValue.type
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue.Type`
        :description: QtCore/QJsonValue-type-f.rst
