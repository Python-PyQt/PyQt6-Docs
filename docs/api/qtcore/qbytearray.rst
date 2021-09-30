:orphan:

.. sip:class:: PyQt6.QtCore.QByteArray
    :description: QtCore/QByteArray-c.rst

    .. sip:enum:: PyQt6.QtCore.QByteArray.Base64DecodingStatus
        :description: QtCore/QByteArray-Base64DecodingStatus-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64DecodingStatus.IllegalCharacter
            :description: QtCore/QByteArray-Base64DecodingStatus-IllegalCharacter-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64DecodingStatus.IllegalInputLength
            :description: QtCore/QByteArray-Base64DecodingStatus-IllegalInputLength-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64DecodingStatus.IllegalPadding
            :description: QtCore/QByteArray-Base64DecodingStatus-IllegalPadding-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64DecodingStatus.Ok
            :description: QtCore/QByteArray-Base64DecodingStatus-Ok-v.rst

    .. sip:enum:: PyQt6.QtCore.QByteArray.Base64Option
        :description: QtCore/QByteArray-Base64Option-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64Option.AbortOnBase64DecodingErrors
            :description: QtCore/QByteArray-Base64Option-AbortOnBase64DecodingErrors-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64Option.Base64Encoding
            :description: QtCore/QByteArray-Base64Option-Base64Encoding-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64Option.Base64UrlEncoding
            :description: QtCore/QByteArray-Base64Option-Base64UrlEncoding-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64Option.IgnoreBase64DecodingErrors
            :description: QtCore/QByteArray-Base64Option-IgnoreBase64DecodingErrors-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64Option.KeepTrailingEquals
            :description: QtCore/QByteArray-Base64Option-KeepTrailingEquals-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QByteArray.Base64Option.OmitTrailingEquals
            :description: QtCore/QByteArray-Base64Option-OmitTrailingEquals-v.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__init__
        :description: QtCore/QByteArray-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__init__
        :args:
            int
            str
        :description: QtCore/QByteArray-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__add__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-__add__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.append
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-append-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.append
        :args:
            int
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-append-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.at
        :args:
            int
        :returns:
            str
        :description: QtCore/QByteArray-at-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.capacity
        :returns:
            int
        :description: QtCore/QByteArray-capacity-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.chop
        :args:
            int
        :description: QtCore/QByteArray-chop-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.chopped
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-chopped-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.clear
        :description: QtCore/QByteArray-clear-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.compare
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            cs: :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity` = :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity.CaseSensitive`
        :returns:
            int
        :description: QtCore/QByteArray-compare-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.contains
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtCore/QByteArray-contains-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__contains__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            int
        :description: QtCore/QByteArray-__contains__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.count
        :returns:
            int
        :description: QtCore/QByteArray-count-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.count
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            int
        :description: QtCore/QByteArray-count-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.data
        :returns:
            bytes
        :description: QtCore/QByteArray-data-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.endsWith
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtCore/QByteArray-endsWith-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__eq__
        :args:
            str
        :returns:
            bool
        :description: QtCore/QByteArray-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__eq__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtCore/QByteArray-__eq__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.fill
        :args:
            str
            size: int = -1
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-fill-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.first
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-first-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.fromBase64
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            options: :sip:ref:`~PyQt6.QtCore.QByteArray.Base64Option` = :sip:ref:`~PyQt6.QtCore.QByteArray.Base64Option.Base64Encoding`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QByteArray-fromBase64-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.fromBase64Encoding
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            options: :sip:ref:`~PyQt6.QtCore.QByteArray.Base64Option` = :sip:ref:`~PyQt6.QtCore.QByteArray.Base64Option.Base64Encoding`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray.FromBase64Result`
        :static:
        :description: QtCore/QByteArray-fromBase64Encoding-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.fromHex
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QByteArray-fromHex-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.fromPercentEncoding
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            percent: str = '%'
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QByteArray-fromPercentEncoding-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__ge__
        :args:
            str
        :returns:
            bool
        :description: QtCore/QByteArray-__ge__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__ge__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtCore/QByteArray-__ge__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__getitem__
        :args:
            int
        :returns:
            str
        :description: QtCore/QByteArray-__getitem__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__getitem__
        :args:
            slice
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-__getitem__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__gt__
        :args:
            str
        :returns:
            bool
        :description: QtCore/QByteArray-__gt__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__gt__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtCore/QByteArray-__gt__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__hash__
        :returns:
            int
        :description: QtCore/QByteArray-__hash__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__iadd__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-__iadd__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__imul__
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-__imul__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.indexOf
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            from: int = 0
        :returns:
            int
        :description: QtCore/QByteArray-indexOf-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.insert
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-insert-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.insert
        :args:
            int
            int
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-insert-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.isEmpty
        :returns:
            bool
        :description: QtCore/QByteArray-isEmpty-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.isLower
        :returns:
            bool
        :description: QtCore/QByteArray-isLower-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.isNull
        :returns:
            bool
        :description: QtCore/QByteArray-isNull-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.isUpper
        :returns:
            bool
        :description: QtCore/QByteArray-isUpper-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.last
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-last-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.lastIndexOf
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            from: int = -1
        :returns:
            int
        :description: QtCore/QByteArray-lastIndexOf-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__le__
        :args:
            str
        :returns:
            bool
        :description: QtCore/QByteArray-__le__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__le__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtCore/QByteArray-__le__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.left
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-left-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.leftJustified
        :args:
            int
            fill: str = ' '
            truncate: bool = False
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-leftJustified-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__len__
        :returns:
            int
        :description: QtCore/QByteArray-__len__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.length
        :returns:
            int
        :description: QtCore/QByteArray-length-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__lt__
        :args:
            str
        :returns:
            bool
        :description: QtCore/QByteArray-__lt__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__lt__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtCore/QByteArray-__lt__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.mid
        :args:
            int
            length: int = -1
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-mid-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__mul__
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-__mul__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__ne__
        :args:
            str
        :returns:
            bool
        :description: QtCore/QByteArray-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__ne__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtCore/QByteArray-__ne__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.number
        :args:
            int
            base: int = 10
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QByteArray-number-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.number
        :args:
            float
            format: str = 'g'
            precision: int = 6
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QByteArray-number-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.prepend
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-prepend-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.prepend
        :args:
            int
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-prepend-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.push_back
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QByteArray-push_back-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.push_front
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtCore/QByteArray-push_front-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.remove
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-remove-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.repeated
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-repeated-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.replace
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-replace-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.replace
        :args:
            int
            int
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-replace-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__repr__
        :returns:
            str
        :description: QtCore/QByteArray-__repr__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.reserve
        :args:
            int
        :description: QtCore/QByteArray-reserve-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.resize
        :args:
            int
        :description: QtCore/QByteArray-resize-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.right
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-right-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.rightJustified
        :args:
            int
            fill: str = ' '
            truncate: bool = False
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-rightJustified-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.setNum
        :args:
            int
            base: int = 10
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-setNum-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.setNum
        :args:
            float
            format: str = 'g'
            precision: int = 6
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-setNum-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.simplified
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-simplified-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.size
        :returns:
            int
        :description: QtCore/QByteArray-size-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.sliced
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-sliced-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.sliced
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-sliced-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.split
        :args:
            str
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtCore/QByteArray-split-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.squeeze
        :description: QtCore/QByteArray-squeeze-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.startsWith
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtCore/QByteArray-startsWith-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.__str__
        :returns:
            str
        :description: QtCore/QByteArray-__str__-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toBase64
        :args:
            options: :sip:ref:`~PyQt6.QtCore.QByteArray.Base64Option` = :sip:ref:`~PyQt6.QtCore.QByteArray.Base64Option.Base64Encoding`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-toBase64-f-1.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toDouble
        :returns:
            float
            bool
        :description: QtCore/QByteArray-toDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toFloat
        :returns:
            float
            bool
        :description: QtCore/QByteArray-toFloat-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toHex
        :args:
            separator: str = '\x00'
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-toHex-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toInt
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toInt-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toLong
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toLong-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toLongLong
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toLongLong-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toLower
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-toLower-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toPercentEncoding
        :args:
            exclude: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
            include: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
            percent: str = '%'
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-toPercentEncoding-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toShort
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toShort-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toUInt
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toUInt-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toULong
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toULong-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toULongLong
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toULongLong-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toUpper
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-toUpper-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.toUShort
        :args:
            base: int = 10
        :returns:
            int
            bool
        :description: QtCore/QByteArray-toUShort-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.trimmed
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QByteArray-trimmed-f.rst

    .. sip:method:: PyQt6.QtCore.QByteArray.truncate
        :args:
            int
        :description: QtCore/QByteArray-truncate-f.rst
