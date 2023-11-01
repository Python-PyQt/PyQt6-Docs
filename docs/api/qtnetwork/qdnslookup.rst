:orphan:

.. sip:class:: PyQt6.QtNetwork.QDnsLookup
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtNetwork/QDnsLookup-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QDnsLookup.Error
        :description: QtNetwork/QDnsLookup-Error-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.InvalidReplyError
            :description: QtNetwork/QDnsLookup-Error-InvalidReplyError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.InvalidRequestError
            :description: QtNetwork/QDnsLookup-Error-InvalidRequestError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.NoError
            :description: QtNetwork/QDnsLookup-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.NotFoundError
            :description: QtNetwork/QDnsLookup-Error-NotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.OperationCancelledError
            :description: QtNetwork/QDnsLookup-Error-OperationCancelledError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.ResolverError
            :description: QtNetwork/QDnsLookup-Error-ResolverError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.ServerFailureError
            :description: QtNetwork/QDnsLookup-Error-ServerFailureError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.ServerRefusedError
            :description: QtNetwork/QDnsLookup-Error-ServerRefusedError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Error.TimeoutError
            :description: QtNetwork/QDnsLookup-Error-TimeoutError-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QDnsLookup.Type
        :description: QtNetwork/QDnsLookup-Type-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.A
            :description: QtNetwork/QDnsLookup-Type-A-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.AAAA
            :description: QtNetwork/QDnsLookup-Type-AAAA-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.ANY
            :description: QtNetwork/QDnsLookup-Type-ANY-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.CNAME
            :description: QtNetwork/QDnsLookup-Type-CNAME-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.MX
            :description: QtNetwork/QDnsLookup-Type-MX-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.NS
            :description: QtNetwork/QDnsLookup-Type-NS-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.PTR
            :description: QtNetwork/QDnsLookup-Type-PTR-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.SRV
            :description: QtNetwork/QDnsLookup-Type-SRV-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QDnsLookup.Type.TXT
            :description: QtNetwork/QDnsLookup-Type-TXT-v.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QDnsLookup-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Type`
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QDnsLookup-__init__-f-3.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Type`
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QDnsLookup-__init__-f-4.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Type`
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            int
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QDnsLookup-__init__-f-5.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.abort
        :description: QtNetwork/QDnsLookup-abort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.canonicalNameRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsDomainNameRecord`]
        :description: QtNetwork/QDnsLookup-canonicalNameRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.error
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Error`
        :description: QtNetwork/QDnsLookup-error-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.errorString
        :returns:
            str
        :description: QtNetwork/QDnsLookup-errorString-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.hostAddressRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsHostAddressRecord`]
        :description: QtNetwork/QDnsLookup-hostAddressRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.isFinished
        :returns:
            bool
        :description: QtNetwork/QDnsLookup-isFinished-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.lookup
        :description: QtNetwork/QDnsLookup-lookup-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.mailExchangeRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsMailExchangeRecord`]
        :description: QtNetwork/QDnsLookup-mailExchangeRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.name
        :returns:
            str
        :description: QtNetwork/QDnsLookup-name-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.nameserver
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
        :description: QtNetwork/QDnsLookup-nameserver-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.nameserverPort
        :returns:
            int
        :description: QtNetwork/QDnsLookup-nameserverPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.nameServerRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsDomainNameRecord`]
        :description: QtNetwork/QDnsLookup-nameServerRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.pointerRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsDomainNameRecord`]
        :description: QtNetwork/QDnsLookup-pointerRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.serviceRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsServiceRecord`]
        :description: QtNetwork/QDnsLookup-serviceRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.setName
        :args:
            Optional[str]
        :description: QtNetwork/QDnsLookup-setName-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.setNameserver
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QDnsLookup-setNameserver-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.setNameserver
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            int
        :description: QtNetwork/QDnsLookup-setNameserver-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.setNameserverPort
        :args:
            int
        :description: QtNetwork/QDnsLookup-setNameserverPort-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.setType
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Type`
        :description: QtNetwork/QDnsLookup-setType-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.textRecords
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QDnsTextRecord`]
        :description: QtNetwork/QDnsLookup-textRecords-f.rst

    .. sip:method:: PyQt6.QtNetwork.QDnsLookup.type
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Type`
        :description: QtNetwork/QDnsLookup-type-f.rst

    .. sip:signal:: PyQt6.QtNetwork.QDnsLookup.finished
        :description: QtNetwork/QDnsLookup-finished-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QDnsLookup.nameChanged
        :args:
            Optional[str]
        :description: QtNetwork/QDnsLookup-nameChanged-s-1.rst

    .. sip:signal:: PyQt6.QtNetwork.QDnsLookup.nameserverChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :description: QtNetwork/QDnsLookup-nameserverChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QDnsLookup.nameserverPortChanged
        :args:
            int
        :description: QtNetwork/QDnsLookup-nameserverPortChanged-s.rst

    .. sip:signal:: PyQt6.QtNetwork.QDnsLookup.typeChanged
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.Type`
        :description: QtNetwork/QDnsLookup-typeChanged-s.rst
