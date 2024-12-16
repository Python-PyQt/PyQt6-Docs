:orphan:

.. sip:class:: PyQt6.QtNetwork.QFormDataBuilder
    :description: QtNetwork/QFormDataBuilder-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QFormDataBuilder.Option
        :description: QtNetwork/QFormDataBuilder-Option-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QFormDataBuilder.Option.Default
            :description: QtNetwork/QFormDataBuilder-Option-Default-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QFormDataBuilder.Option.OmitRfc8187EncodedFilename
            :description: QtNetwork/QFormDataBuilder-Option-OmitRfc8187EncodedFilename-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QFormDataBuilder.Option.PreferLatin1EncodedFilename
            :description: QtNetwork/QFormDataBuilder-Option-PreferLatin1EncodedFilename-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QFormDataBuilder.Option.StrictRfc7578
            :description: QtNetwork/QFormDataBuilder-Option-StrictRfc7578-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QFormDataBuilder.Option.UseRfc7578PercentEncodedFilename
            :description: QtNetwork/QFormDataBuilder-Option-UseRfc7578PercentEncodedFilename-v.rst

    .. sip:method:: PyQt6.QtNetwork.QFormDataBuilder.__init__
        :description: QtNetwork/QFormDataBuilder-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QFormDataBuilder.buildMultiPart
        :args:
            options: :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder.Option` = {}
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart`
        :description: QtNetwork/QFormDataBuilder-buildMultiPart-f.rst

    .. sip:method:: PyQt6.QtNetwork.QFormDataBuilder.part
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QFormDataPartBuilder`
        :description: QtNetwork/QFormDataBuilder-part-f.rst

    .. sip:method:: PyQt6.QtNetwork.QFormDataBuilder.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder`
        :description: QtNetwork/QFormDataBuilder-swap-f.rst
