:orphan:

.. sip:class:: PyQt6.QtCore.QJsonDocument
    :description: QtCore/QJsonDocument-c.rst

    .. sip:enum:: PyQt6.QtCore.QJsonDocument.JsonFormat
        :description: QtCore/QJsonDocument-JsonFormat-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonDocument.JsonFormat.Compact
            :description: QtCore/QJsonDocument-JsonFormat-Compact-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QJsonDocument.JsonFormat.Indented
            :description: QtCore/QJsonDocument-JsonFormat-Indented-v.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__init__
        :description: QtCore/QJsonDocument-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__init__
        :args:
            dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None]
        :description: QtCore/QJsonDocument-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__init__
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None]
        :description: QtCore/QJsonDocument-__init__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :description: QtCore/QJsonDocument-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.array
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QJsonValue`]
        :description: QtCore/QJsonDocument-array-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__eq__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :returns:
            bool
        :description: QtCore/QJsonDocument-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.fromJson
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`|bytes|bytearray|memoryview
            error: :sip:ref:`~PyQt6.QtCore.QJsonParseError` = None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :static:
        :description: QtCore/QJsonDocument-fromJson-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.fromVariant
        :args:
            Any
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :static:
        :description: QtCore/QJsonDocument-fromVariant-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__getitem__
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :description: QtCore/QJsonDocument-__getitem__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__getitem__
        :args:
            str|None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :description: QtCore/QJsonDocument-__getitem__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.isArray
        :returns:
            bool
        :description: QtCore/QJsonDocument-isArray-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.isEmpty
        :returns:
            bool
        :description: QtCore/QJsonDocument-isEmpty-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.isNull
        :returns:
            bool
        :description: QtCore/QJsonDocument-isNull-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.isObject
        :returns:
            bool
        :description: QtCore/QJsonDocument-isObject-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.__ne__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :returns:
            bool
        :description: QtCore/QJsonDocument-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.object
        :returns:
            dict[str, :sip:ref:`~PyQt6.QtCore.QJsonValue`]
        :description: QtCore/QJsonDocument-object-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.setArray
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None]
        :description: QtCore/QJsonDocument-setArray-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.setObject
        :args:
            dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`|:sip:ref:`~PyQt6.QtCore.QJsonValue.Type`|Iterable[:sip:ref:`~PyQt6.QtCore.QJsonValue`]|dict[str|None, :sip:ref:`~PyQt6.QtCore.QJsonValue`]|bool|int|float|None|str|None]
        :description: QtCore/QJsonDocument-setObject-f-1.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :description: QtCore/QJsonDocument-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.toJson
        :args:
            format: :sip:ref:`~PyQt6.QtCore.QJsonDocument.JsonFormat` = :sip:ref:`~PyQt6.QtCore.QJsonDocument.JsonFormat.Indented`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QJsonDocument-toJson-f.rst

    .. sip:method:: PyQt6.QtCore.QJsonDocument.toVariant
        :returns:
            Any
        :description: QtCore/QJsonDocument-toVariant-f.rst
