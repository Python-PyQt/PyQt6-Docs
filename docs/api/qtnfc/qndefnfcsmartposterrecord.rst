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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNfc/QNdefNfcSmartPosterRecord-addIcon-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.addTitle
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-addTitle-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.addTitle
        :args:
            str
            str
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord.Encoding`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-addTitle-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasAction
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasAction-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasIcon
        :args:
            mimetype: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasIcon-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasSize
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasSize-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasTitle
        :args:
            locale: str = ''
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasTitle-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.hasTypeInfo
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-hasTypeInfo-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.icon
        :args:
            mimetype: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNfc/QNdefNfcSmartPosterRecord-icon-f.rst

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
            List[:sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`]
        :description: QtNfc/QNdefNfcSmartPosterRecord-iconRecords-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeIcon
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcIconRecord`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeIcon-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeIcon
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeIcon-f-1.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeTitle
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeTitle-f.rst

    .. sip:method:: PyQt6.QtNfc.QNdefNfcSmartPosterRecord.removeTitle
        :args:
            str
        :returns:
            bool
        :description: QtNfc/QNdefNfcSmartPosterRecord-removeTitle-f-1.rst

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
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNfc/QNdefNfcSmartPosterRecord-setPayload-f.rst

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
            str
        :description: QtNfc/QNdefNfcSmartPosterRecord-setTypeInfo-f.rst

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
            locale: str = ''
        :returns:
            str
        :description: QtNfc/QNdefNfcSmartPosterRecord-title-f.rst

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
            List[:sip:ref:`~PyQt6.QtNfc.QNdefNfcTextRecord`]
        :description: QtNfc/QNdefNfcSmartPosterRecord-titleRecords-f.rst

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
