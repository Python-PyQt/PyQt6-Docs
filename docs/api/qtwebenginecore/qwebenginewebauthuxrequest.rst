:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError.InternalUvLocked
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-InternalUvLocked-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError.InvalidCharacters
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-InvalidCharacters-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError.NoError
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError.SameAsCurrentPin
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-SameAsCurrentPin-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError.TooShort
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-TooShort-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryError.WrongPin
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryError-WrongPin-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryReason
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryReason-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryReason.Challenge
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryReason-Challenge-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryReason.Change
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryReason-Change-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.PinEntryReason.Set
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-PinEntryReason-Set-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.AuthenticatorMissingLargeBlob
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-AuthenticatorMissingLargeBlob-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.AuthenticatorMissingResidentKeys
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-AuthenticatorMissingResidentKeys-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.AuthenticatorMissingUserVerification
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-AuthenticatorMissingUserVerification-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.AuthenticatorRemovedDuringPinEntry
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-AuthenticatorRemovedDuringPinEntry-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.HardPinBlock
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-HardPinBlock-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.KeyAlreadyRegistered
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-KeyAlreadyRegistered-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.KeyNotRegistered
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-KeyNotRegistered-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.NoCommonAlgorithms
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-NoCommonAlgorithms-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.SoftPinBlock
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-SoftPinBlock-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.StorageFull
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-StorageFull-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.Timeout
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-Timeout-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.UserConsentDenied
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-UserConsentDenied-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason.WinUserCancelled
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-RequestFailureReason-WinUserCancelled-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.Cancelled
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-Cancelled-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.CollectPin
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-CollectPin-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.Completed
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-Completed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.FinishTokenCollection
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-FinishTokenCollection-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.NotStarted
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-NotStarted-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.RequestFailed
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-RequestFailed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.SelectAccount
            :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-WebAuthUxState-SelectAccount-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.cancel
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-cancel-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.pinRequest
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthPinRequest`
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-pinRequest-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.relyingPartyId
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-relyingPartyId-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.requestFailureReason
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.RequestFailureReason`
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-requestFailureReason-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.retry
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-retry-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.setPin
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-setPin-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.setSelectedAccount
        :args:
            Optional[str]
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-setSelectedAccount-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.state
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState`
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-state-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.userNames
        :returns:
            list[str]
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-userNames-f.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState`
        :description: QtWebEngineCore/QWebEngineWebAuthUxRequest-stateChanged-s.rst
