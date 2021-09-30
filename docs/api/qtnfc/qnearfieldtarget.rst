:orphan:

.. sip:class:: PyQt6.QtNfc.QNearFieldTarget
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNfc/QNearFieldTarget-c.rst

    .. sip:enum:: PyQt6.QtNfc.QNearFieldTarget.AccessMethod
        :description: QtNfc/QNearFieldTarget-AccessMethod-e.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.AccessMethod.AnyAccess
            :description: QtNfc/QNearFieldTarget-AccessMethod-AnyAccess-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.AccessMethod.NdefAccess
            :description: QtNfc/QNearFieldTarget-AccessMethod-NdefAccess-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.AccessMethod.TagTypeSpecificAccess
            :description: QtNfc/QNearFieldTarget-AccessMethod-TagTypeSpecificAccess-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.AccessMethod.UnknownAccess
            :description: QtNfc/QNearFieldTarget-AccessMethod-UnknownAccess-v.rst

    .. sip:enum:: PyQt6.QtNfc.QNearFieldTarget.Error
        :description: QtNfc/QNearFieldTarget-Error-e.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.ChecksumMismatchError
            :description: QtNfc/QNearFieldTarget-Error-ChecksumMismatchError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.CommandError
            :description: QtNfc/QNearFieldTarget-Error-CommandError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.ConnectionError
            :description: QtNfc/QNearFieldTarget-Error-ConnectionError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.InvalidParametersError
            :description: QtNfc/QNearFieldTarget-Error-InvalidParametersError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.NdefReadError
            :description: QtNfc/QNearFieldTarget-Error-NdefReadError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.NdefWriteError
            :description: QtNfc/QNearFieldTarget-Error-NdefWriteError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.NoError
            :description: QtNfc/QNearFieldTarget-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.NoResponseError
            :description: QtNfc/QNearFieldTarget-Error-NoResponseError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.TargetOutOfRangeError
            :description: QtNfc/QNearFieldTarget-Error-TargetOutOfRangeError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.TimeoutError
            :description: QtNfc/QNearFieldTarget-Error-TimeoutError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.UnknownError
            :description: QtNfc/QNearFieldTarget-Error-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Error.UnsupportedError
            :description: QtNfc/QNearFieldTarget-Error-UnsupportedError-v.rst

    .. sip:enum:: PyQt6.QtNfc.QNearFieldTarget.Type
        :description: QtNfc/QNearFieldTarget-Type-e.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.MifareTag
            :description: QtNfc/QNearFieldTarget-Type-MifareTag-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.NfcTagType1
            :description: QtNfc/QNearFieldTarget-Type-NfcTagType1-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.NfcTagType2
            :description: QtNfc/QNearFieldTarget-Type-NfcTagType2-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.NfcTagType3
            :description: QtNfc/QNearFieldTarget-Type-NfcTagType3-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.NfcTagType4
            :description: QtNfc/QNearFieldTarget-Type-NfcTagType4-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.NfcTagType4A
            :description: QtNfc/QNearFieldTarget-Type-NfcTagType4A-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.NfcTagType4B
            :description: QtNfc/QNearFieldTarget-Type-NfcTagType4B-v.rst

        .. sip:enum-member:: PyQt6.QtNfc.QNearFieldTarget.Type.ProprietaryTag
            :description: QtNfc/QNearFieldTarget-Type-ProprietaryTag-v.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNfc/QNearFieldTarget-__init__-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.accessMethods
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.AccessMethod`
        :description: QtNfc/QNearFieldTarget-accessMethods-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.disconnect
        :returns:
            bool
        :description: QtNfc/QNearFieldTarget-disconnect-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.hasNdefMessage
        :returns:
            bool
        :description: QtNfc/QNearFieldTarget-hasNdefMessage-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.maxCommandLength
        :returns:
            int
        :description: QtNfc/QNearFieldTarget-maxCommandLength-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.readNdefMessages
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
        :description: QtNfc/QNearFieldTarget-readNdefMessages-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.requestResponse
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
        :returns:
            Any
        :description: QtNfc/QNearFieldTarget-requestResponse-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.sendCommand
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
        :description: QtNfc/QNearFieldTarget-sendCommand-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.type
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.Type`
        :description: QtNfc/QNearFieldTarget-type-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.uid
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNfc/QNearFieldTarget-uid-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.waitForRequestCompleted
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
            msecs: int = 5000
        :returns:
            bool
        :description: QtNfc/QNearFieldTarget-waitForRequestCompleted-f.rst

    .. sip:method:: PyQt6.QtNfc.QNearFieldTarget.writeNdefMessages
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNfc.QNdefMessage`]
        :returns:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
        :description: QtNfc/QNearFieldTarget-writeNdefMessages-f.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldTarget.disconnected
        :description: QtNfc/QNearFieldTarget-disconnected-s.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldTarget.error
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.Error`
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
        :description: QtNfc/QNearFieldTarget-error-s.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldTarget.ndefMessageRead
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNdefMessage`
        :description: QtNfc/QNearFieldTarget-ndefMessageRead-s.rst

    .. sip:signal:: PyQt6.QtNfc.QNearFieldTarget.requestCompleted
        :args:
            :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget.RequestId`
        :description: QtNfc/QNearFieldTarget-requestCompleted-s.rst
