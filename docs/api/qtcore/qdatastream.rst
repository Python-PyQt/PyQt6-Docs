:orphan:

.. sip:class:: PyQt6.QtCore.QDataStream
    :inherits: :sip:ref:`~PyQt6.QtCore.QIODeviceBase`
    :description: QtCore/QDataStream-c.rst

    .. sip:enum:: PyQt6.QtCore.QDataStream.ByteOrder
        :description: QtCore/QDataStream-ByteOrder-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.ByteOrder.BigEndian
            :description: QtCore/QDataStream-ByteOrder-BigEndian-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.ByteOrder.LittleEndian
            :description: QtCore/QDataStream-ByteOrder-LittleEndian-v.rst

    .. sip:enum:: PyQt6.QtCore.QDataStream.FloatingPointPrecision
        :description: QtCore/QDataStream-FloatingPointPrecision-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.FloatingPointPrecision.DoublePrecision
            :description: QtCore/QDataStream-FloatingPointPrecision-DoublePrecision-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.FloatingPointPrecision.SinglePrecision
            :description: QtCore/QDataStream-FloatingPointPrecision-SinglePrecision-v.rst

    .. sip:enum:: PyQt6.QtCore.QDataStream.Status
        :description: QtCore/QDataStream-Status-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Status.Ok
            :description: QtCore/QDataStream-Status-Ok-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Status.ReadCorruptData
            :description: QtCore/QDataStream-Status-ReadCorruptData-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Status.ReadPastEnd
            :description: QtCore/QDataStream-Status-ReadPastEnd-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Status.WriteFailed
            :description: QtCore/QDataStream-Status-WriteFailed-v.rst

    .. sip:enum:: PyQt6.QtCore.QDataStream.Version
        :description: QtCore/QDataStream-Version-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_1_0
            :description: QtCore/QDataStream-Version-Qt_1_0-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_2_0
            :description: QtCore/QDataStream-Version-Qt_2_0-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_2_1
            :description: QtCore/QDataStream-Version-Qt_2_1-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_3_0
            :description: QtCore/QDataStream-Version-Qt_3_0-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_3_1
            :description: QtCore/QDataStream-Version-Qt_3_1-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_3_3
            :description: QtCore/QDataStream-Version-Qt_3_3-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_0
            :description: QtCore/QDataStream-Version-Qt_4_0-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_1
            :description: QtCore/QDataStream-Version-Qt_4_1-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_2
            :description: QtCore/QDataStream-Version-Qt_4_2-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_3
            :description: QtCore/QDataStream-Version-Qt_4_3-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_4
            :description: QtCore/QDataStream-Version-Qt_4_4-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_5
            :description: QtCore/QDataStream-Version-Qt_4_5-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_6
            :description: QtCore/QDataStream-Version-Qt_4_6-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_7
            :description: QtCore/QDataStream-Version-Qt_4_7-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_8
            :description: QtCore/QDataStream-Version-Qt_4_8-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_4_9
            :description: QtCore/QDataStream-Version-Qt_4_9-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_0
            :description: QtCore/QDataStream-Version-Qt_5_0-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_1
            :description: QtCore/QDataStream-Version-Qt_5_1-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_10
            :description: QtCore/QDataStream-Version-Qt_5_10-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_11
            :description: QtCore/QDataStream-Version-Qt_5_11-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_12
            :description: QtCore/QDataStream-Version-Qt_5_12-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_13
            :description: QtCore/QDataStream-Version-Qt_5_13-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_14
            :description: QtCore/QDataStream-Version-Qt_5_14-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_15
            :description: QtCore/QDataStream-Version-Qt_5_15-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_2
            :description: QtCore/QDataStream-Version-Qt_5_2-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_3
            :description: QtCore/QDataStream-Version-Qt_5_3-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_4
            :description: QtCore/QDataStream-Version-Qt_5_4-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_5
            :description: QtCore/QDataStream-Version-Qt_5_5-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_6
            :description: QtCore/QDataStream-Version-Qt_5_6-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_7
            :description: QtCore/QDataStream-Version-Qt_5_7-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_8
            :description: QtCore/QDataStream-Version-Qt_5_8-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_5_9
            :description: QtCore/QDataStream-Version-Qt_5_9-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_6_0
            :description: QtCore/QDataStream-Version-Qt_6_0-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_6_1
            :description: QtCore/QDataStream-Version-Qt_6_1-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_6_2
            :description: QtCore/QDataStream-Version-Qt_6_2-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_6_3
            :description: QtCore/QDataStream-Version-Qt_6_3-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDataStream.Version.Qt_6_4
            :description: QtCore/QDataStream-Version-Qt_6_4-v.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__init__
        :description: QtCore/QDataStream-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QDataStream-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QDataStream-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag`
        :description: QtCore/QDataStream-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.abortTransaction
        :description: QtCore/QDataStream-abortTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.atEnd
        :returns:
            bool
        :description: QtCore/QDataStream-atEnd-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.byteOrder
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream.ByteOrder`
        :description: QtCore/QDataStream-byteOrder-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.commitTransaction
        :returns:
            bool
        :description: QtCore/QDataStream-commitTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QDataStream-device-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.floatingPointPrecision
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream.FloatingPointPrecision`
        :description: QtCore/QDataStream-floatingPointPrecision-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QBitArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QKeyCombination`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QTime`, datetime.time]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QEasingCurve`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-6.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-7.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-8.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QLine`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-9.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QLineF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-10.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-11.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-12.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-13.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-14.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-15.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-16.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-17.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-18.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-19.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-20.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-21.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-22.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUuid`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-23.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QVariant`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-27.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTypeRevision`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-25.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QVersionNumber`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__lshift__-f-26.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readBool
        :returns:
            bool
        :description: QtCore/QDataStream-readBool-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readBytes
        :returns:
            bytes
        :description: QtCore/QDataStream-readBytes-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readDouble
        :returns:
            float
        :description: QtCore/QDataStream-readDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readFloat
        :returns:
            float
        :description: QtCore/QDataStream-readFloat-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readInt
        :returns:
            int
        :description: QtCore/QDataStream-readInt-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readInt16
        :returns:
            int
        :description: QtCore/QDataStream-readInt16-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readInt32
        :returns:
            int
        :description: QtCore/QDataStream-readInt32-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readInt64
        :returns:
            int
        :description: QtCore/QDataStream-readInt64-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readInt8
        :returns:
            int
        :description: QtCore/QDataStream-readInt8-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readQString
        :returns:
            str
        :description: QtCore/QDataStream-readQString-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readQStringList
        :returns:
            List[str]
        :description: QtCore/QDataStream-readQStringList-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readQVariant
        :returns:
            Any
        :description: QtCore/QDataStream-readQVariant-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readQVariantHash
        :returns:
            Dict[str, Any]
        :description: QtCore/QDataStream-readQVariantHash-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readQVariantList
        :returns:
            List[Any]
        :description: QtCore/QDataStream-readQVariantList-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readQVariantMap
        :returns:
            Dict[str, Any]
        :description: QtCore/QDataStream-readQVariantMap-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readRawData
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QDataStream-readRawData-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readString
        :returns:
            bytes
        :description: QtCore/QDataStream-readString-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readUInt16
        :returns:
            int
        :description: QtCore/QDataStream-readUInt16-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readUInt32
        :returns:
            int
        :description: QtCore/QDataStream-readUInt32-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readUInt64
        :returns:
            int
        :description: QtCore/QDataStream-readUInt64-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.readUInt8
        :returns:
            int
        :description: QtCore/QDataStream-readUInt8-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.resetStatus
        :description: QtCore/QDataStream-resetStatus-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.rollbackTransaction
        :description: QtCore/QDataStream-rollbackTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QBitArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QKeyCombination`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTime`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QEasingCurve`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-6.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonDocument`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-7.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QJsonValue`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-8.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QLine`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-9.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QLineF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-10.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-11.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-12.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-13.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-14.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-15.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-16.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-17.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-18.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-19.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-20.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-21.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-22.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUuid`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-23.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QVariant`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-24.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QTypeRevision`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-25.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.__rshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QVersionNumber`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-__rshift__-f-26.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.setByteOrder
        :args:
            :sip:ref:`~PyQt6.QtCore.QDataStream.ByteOrder`
        :description: QtCore/QDataStream-setByteOrder-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtCore/QDataStream-setDevice-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.setFloatingPointPrecision
        :args:
            :sip:ref:`~PyQt6.QtCore.QDataStream.FloatingPointPrecision`
        :description: QtCore/QDataStream-setFloatingPointPrecision-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.setStatus
        :args:
            :sip:ref:`~PyQt6.QtCore.QDataStream.Status`
        :description: QtCore/QDataStream-setStatus-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.setVersion
        :args:
            int
        :description: QtCore/QDataStream-setVersion-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.skipRawData
        :args:
            int
        :returns:
            int
        :description: QtCore/QDataStream-skipRawData-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.startTransaction
        :description: QtCore/QDataStream-startTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.status
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream.Status`
        :description: QtCore/QDataStream-status-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.version
        :returns:
            int
        :description: QtCore/QDataStream-version-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeBool
        :args:
            bool
        :description: QtCore/QDataStream-writeBool-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeBytes
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QDataStream-writeBytes-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeDouble
        :args:
            float
        :description: QtCore/QDataStream-writeDouble-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeFloat
        :args:
            float
        :description: QtCore/QDataStream-writeFloat-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeInt
        :args:
            int
        :description: QtCore/QDataStream-writeInt-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeInt16
        :args:
            int
        :description: QtCore/QDataStream-writeInt16-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeInt32
        :args:
            int
        :description: QtCore/QDataStream-writeInt32-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeInt64
        :args:
            int
        :description: QtCore/QDataStream-writeInt64-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeInt8
        :args:
            int
        :description: QtCore/QDataStream-writeInt8-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeQString
        :args:
            str
        :description: QtCore/QDataStream-writeQString-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeQStringList
        :args:
            Iterable[str]
        :description: QtCore/QDataStream-writeQStringList-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeQVariant
        :args:
            Any
        :description: QtCore/QDataStream-writeQVariant-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeQVariantHash
        :args:
            Dict[str, Any]
        :description: QtCore/QDataStream-writeQVariantHash-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeQVariantList
        :args:
            Iterable[Any]
        :description: QtCore/QDataStream-writeQVariantList-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeQVariantMap
        :args:
            Dict[str, Any]
        :description: QtCore/QDataStream-writeQVariantMap-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeRawData
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
        :returns:
            int
        :description: QtCore/QDataStream-writeRawData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeString
        :args:
            bytes
        :description: QtCore/QDataStream-writeString-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeUInt16
        :args:
            int
        :description: QtCore/QDataStream-writeUInt16-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeUInt32
        :args:
            int
        :description: QtCore/QDataStream-writeUInt32-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeUInt64
        :args:
            int
        :description: QtCore/QDataStream-writeUInt64-f.rst

    .. sip:method:: PyQt6.QtCore.QDataStream.writeUInt8
        :args:
            int
        :description: QtCore/QDataStream-writeUInt8-f.rst
