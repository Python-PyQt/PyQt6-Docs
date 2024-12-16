:orphan:

.. sip:class:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord
    :inherits: :sip:ref:`~PyQt6.QtNfc.QNdefRecord`
    :description: QtNfc/QNdefNfcSmartPosterRecord-c.rst

    .. sip:enum:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action
        :description: QtNfc/QNdefNfcSmartPosterRecord-Action-e.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action.DoAction
            :description: QtNfc/QNdefNfcSmartPosterRecord-Action-DoAction-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action.EditAction
            :description: QtNfc/QNdefNfcSmartPosterRecord-Action-EditAction-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action.SaveAction
            :description: QtNfc/QNdefNfcSmartPosterRecord-Action-SaveAction-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action.UnspecifiedAction
            :description: QtNfc/QNdefNfcSmartPosterRecord-Action-UnspecifiedAction-v.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.__init__
        :description: QtNfc/QNdefNfcSmartPosterRecord-__init__-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.__init__
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcSmartPosterRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.__init__
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-__init__-f-2.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.action
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action`
        :description: QtNfc/QNdefNfcSmartPosterRecord-action-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.addIcon
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-addIcon-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.addIcon
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtNfc/QNdefNfcSmartPosterRecord-addIcon-f-2.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.addTitle
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-addTitle-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.addTitle
        :args:
            Optional[str]
            Optional[str]
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord.Encoding`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-addTitle-f-2.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasAction
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasAction-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasIcon
        :args:
            mimetype: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasIcon-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasSize
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasSize-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasTitle
        :args:
            locale: Optional[str] = ''
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasTitle-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasTypeInfo
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasTypeInfo-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.icon
        :args:
            mimetype: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNfc/QNdefNfcSmartPosterRecord-icon-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.iconCount
        :returns:
            int
        :description: QtNfc/QNdefNfcSmartPosterRecord-iconCount-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.iconRecord
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-iconRecord-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.iconRecords
        :returns:
            list[:sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`]
        :description: QtNfc/QNdefNfcSmartPosterRecord-iconRecords-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeIcon
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeIcon-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeIcon
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeIcon-f-2.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeTitle
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeTitle-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeTitle
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeTitle-f-2.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setAction
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcSmartPosterRecord.Action`
        :description: QtNfc/QNdefNfcSmartPosterRecord-setAction-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setIcons
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`]
        :description: QtNfc/QNdefNfcSmartPosterRecord-setIcons-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setPayload
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtNfc/QNdefNfcSmartPosterRecord-setPayload-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setSize
        :args:
            int
        :description: QtNfc/QNdefNfcSmartPosterRecord-setSize-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setTitles
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`]
        :description: QtNfc/QNdefNfcSmartPosterRecord-setTitles-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setTypeInfo
        :args:
            Optional[str]
        :description: QtNfc/QNdefNfcSmartPosterRecord-setTypeInfo-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setUri
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcUriRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-setUri-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.setUri
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNfc/QNdefNfcSmartPosterRecord-setUri-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.size
        :returns:
            int
        :description: QtNfc/QNdefNfcSmartPosterRecord-size-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.title
        :args:
            locale: Optional[str] = ''
        :returns:
            str
        :description: QtNfc/QNdefNfcSmartPosterRecord-title-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.titleCount
        :returns:
            int
        :description: QtNfc/QNdefNfcSmartPosterRecord-titleCount-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.titleRecord
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-titleRecord-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.titleRecords
        :returns:
            list[:sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`]
        :description: QtNfc/QNdefNfcSmartPosterRecord-titleRecords-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.typeInfo
        :returns:
            str
        :description: QtNfc/QNdefNfcSmartPosterRecord-typeInfo-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.uri
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNfc/QNdefNfcSmartPosterRecord-uri-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.uriRecord
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcUriRecord`
        :description: QtNfc/QNdefNfcSmartPosterRecord-uriRecord-f.rst
