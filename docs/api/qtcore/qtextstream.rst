:orphan:

.. sip:class:: PyQt6.QtCore.QTextStream
    :inherits: :sip:ref:`~PyQt6.QtCore.QIODeviceBase`
    :description: QtCore/QTextStream-c.rst

    .. sip:enum:: PyQt6.QtCore.QTextStream.FieldAlignment
        :description: QtCore/QTextStream-FieldAlignment-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.FieldAlignment.AlignAccountingStyle
            :description: QtCore/QTextStream-FieldAlignment-AlignAccountingStyle-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.FieldAlignment.AlignCenter
            :description: QtCore/QTextStream-FieldAlignment-AlignCenter-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.FieldAlignment.AlignLeft
            :description: QtCore/QTextStream-FieldAlignment-AlignLeft-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.FieldAlignment.AlignRight
            :description: QtCore/QTextStream-FieldAlignment-AlignRight-v.rst

    .. sip:enum:: PyQt6.QtCore.QTextStream.NumberFlag
        :description: QtCore/QTextStream-NumberFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.NumberFlag.ForcePoint
            :description: QtCore/QTextStream-NumberFlag-ForcePoint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.NumberFlag.ForceSign
            :description: QtCore/QTextStream-NumberFlag-ForceSign-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.NumberFlag.ShowBase
            :description: QtCore/QTextStream-NumberFlag-ShowBase-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.NumberFlag.UppercaseBase
            :description: QtCore/QTextStream-NumberFlag-UppercaseBase-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.NumberFlag.UppercaseDigits
            :description: QtCore/QTextStream-NumberFlag-UppercaseDigits-v.rst

    .. sip:enum:: PyQt6.QtCore.QTextStream.RealNumberNotation
        :description: QtCore/QTextStream-RealNumberNotation-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.RealNumberNotation.FixedNotation
            :description: QtCore/QTextStream-RealNumberNotation-FixedNotation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.RealNumberNotation.ScientificNotation
            :description: QtCore/QTextStream-RealNumberNotation-ScientificNotation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.RealNumberNotation.SmartNotation
            :description: QtCore/QTextStream-RealNumberNotation-SmartNotation-v.rst

    .. sip:enum:: PyQt6.QtCore.QTextStream.Status
        :description: QtCore/QTextStream-Status-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.Status.Ok
            :description: QtCore/QTextStream-Status-Ok-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.Status.ReadCorruptData
            :description: QtCore/QTextStream-Status-ReadCorruptData-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.Status.ReadPastEnd
            :description: QtCore/QTextStream-Status-ReadPastEnd-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QTextStream.Status.WriteFailed
            :description: QtCore/QTextStream-Status-WriteFailed-v.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__init__
        :description: QtCore/QTextStream-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QTextStream-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :description: QtCore/QTextStream-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.atEnd
        :returns:
            bool
        :description: QtCore/QTextStream-atEnd-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.autoDetectUnicode
        :returns:
            bool
        :description: QtCore/QTextStream-autoDetectUnicode-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QTextStream-device-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.encoding
        :returns:
            :sip:ref:`~PyQt6.QtCore.QStringConverter.Encoding`
        :description: QtCore/QTextStream-encoding-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.fieldAlignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream.FieldAlignment`
        :description: QtCore/QTextStream-fieldAlignment-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.fieldWidth
        :returns:
            int
        :description: QtCore/QTextStream-fieldWidth-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.flush
        :description: QtCore/QTextStream-flush-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.generateByteOrderMark
        :returns:
            bool
        :description: QtCore/QTextStream-generateByteOrderMark-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__int__
        :returns:
            bool
        :description: QtCore/QTextStream-__int__-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.integerBase
        :returns:
            int
        :description: QtCore/QTextStream-integerBase-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtCore/QTextStream-locale-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__lshift__
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
        :description: QtCore/QTextStream-__lshift__-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__lshift__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
        :description: QtCore/QTextStream-__lshift__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__lshift__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
        :description: QtCore/QTextStream-__lshift__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__lshift__
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
        :description: QtCore/QTextStream-__lshift__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextStreamManipulator`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
        :description: QtCore/QTextStream-__lshift__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.numberFlags
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlag`
        :description: QtCore/QTextStream-numberFlags-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.padChar
        :returns:
            str
        :description: QtCore/QTextStream-padChar-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.pos
        :returns:
            int
        :description: QtCore/QTextStream-pos-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.read
        :args:
            int
        :returns:
            str
        :description: QtCore/QTextStream-read-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.readAll
        :returns:
            str
        :description: QtCore/QTextStream-readAll-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.readLine
        :args:
            maxLength: int = 0
        :returns:
            str
        :description: QtCore/QTextStream-readLine-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.realNumberNotation
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation`
        :description: QtCore/QTextStream-realNumberNotation-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.realNumberPrecision
        :returns:
            int
        :description: QtCore/QTextStream-realNumberPrecision-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.reset
        :description: QtCore/QTextStream-reset-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.resetStatus
        :description: QtCore/QTextStream-resetStatus-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream`
        :description: QtCore/QTextStream-__rshift__-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.seek
        :args:
            int
        :returns:
            bool
        :description: QtCore/QTextStream-seek-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setAutoDetectUnicode
        :args:
            bool
        :description: QtCore/QTextStream-setAutoDetectUnicode-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QTextStream-setDevice-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setEncoding
        :args:
            :sip:ref:`~PyQt6.QtCore.QStringConverter.Encoding`
        :description: QtCore/QTextStream-setEncoding-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setFieldAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextStream.FieldAlignment`
        :description: QtCore/QTextStream-setFieldAlignment-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setFieldWidth
        :args:
            int
        :description: QtCore/QTextStream-setFieldWidth-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setGenerateByteOrderMark
        :args:
            bool
        :description: QtCore/QTextStream-setGenerateByteOrderMark-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setIntegerBase
        :args:
            int
        :description: QtCore/QTextStream-setIntegerBase-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setLocale
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtCore/QTextStream-setLocale-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setNumberFlags
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlag`
        :description: QtCore/QTextStream-setNumberFlags-f-1.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setPadChar
        :args:
            str
        :description: QtCore/QTextStream-setPadChar-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setRealNumberNotation
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation`
        :description: QtCore/QTextStream-setRealNumberNotation-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setRealNumberPrecision
        :args:
            int
        :description: QtCore/QTextStream-setRealNumberPrecision-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.setStatus
        :args:
            :sip:ref:`~PyQt6.QtCore.QTextStream.Status`
        :description: QtCore/QTextStream-setStatus-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.skipWhiteSpace
        :description: QtCore/QTextStream-skipWhiteSpace-f.rst

    .. sip:method:: PyQt6.QtCore.QTextStream.status
        :returns:
            :sip:ref:`~PyQt6.QtCore.QTextStream.Status`
        :description: QtCore/QTextStream-status-f.rst
