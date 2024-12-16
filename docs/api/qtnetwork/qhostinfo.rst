:orphan:

.. sip:class:: PyQt6.QtNetwork.QHostInfo
    :description: QtNetwork/QHostInfo-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QHostInfo.HostInfoError
        :description: QtNetwork/QHostInfo-HostInfoError-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostInfo.HostInfoError.HostNotFound
            :description: QtNetwork/QHostInfo-HostInfoError-HostNotFound-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostInfo.HostInfoError.NoError
            :description: QtNetwork/QHostInfo-HostInfoError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QHostInfo.HostInfoError.UnknownError
            :description: QtNetwork/QHostInfo-HostInfoError-UnknownError-v.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.__init__
        :args:
            id: int = -1
        :description: QtNetwork/QHostInfo-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostInfo`
        :description: QtNetwork/QHostInfo-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.abortHostLookup
        :args:
            int
        :static:
        :description: QtNetwork/QHostInfo-abortHostLookup-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.addresses
        :returns:
            list[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`]
        :description: QtNetwork/QHostInfo-addresses-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.error
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostInfo.HostInfoError`
        :description: QtNetwork/QHostInfo-error-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.errorString
        :returns:
            str
        :description: QtNetwork/QHostInfo-errorString-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.fromName
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostInfo`
        :static:
        :description: QtNetwork/QHostInfo-fromName-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.hostName
        :returns:
            str
        :description: QtNetwork/QHostInfo-hostName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.localDomainName
        :returns:
            str
        :static:
        :description: QtNetwork/QHostInfo-localDomainName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.localHostName
        :returns:
            str
        :static:
        :description: QtNetwork/QHostInfo-localHostName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.lookupHost
        :args:
            Optional[str]
            PYQT_SLOT
        :returns:
            int
        :static:
        :description: QtNetwork/QHostInfo-lookupHost-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.lookupId
        :returns:
            int
        :description: QtNetwork/QHostInfo-lookupId-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.setAddresses
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]]
        :description: QtNetwork/QHostInfo-setAddresses-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.setError
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostInfo.HostInfoError`
        :description: QtNetwork/QHostInfo-setError-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.setErrorString
        :args:
            Optional[str]
        :description: QtNetwork/QHostInfo-setErrorString-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.setHostName
        :args:
            Optional[str]
        :description: QtNetwork/QHostInfo-setHostName-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.setLookupId
        :args:
            int
        :description: QtNetwork/QHostInfo-setLookupId-f.rst

    .. sip:method:: PyQt6.QtNetwork.QHostInfo.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QHostInfo`
        :description: QtNetwork/QHostInfo-swap-f.rst
