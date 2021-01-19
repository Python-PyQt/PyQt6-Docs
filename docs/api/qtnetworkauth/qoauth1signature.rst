:orphan:

.. sip:class:: PyQt6.QtNetworkAuth.QOAuth1Signature
    :description: QtNetworkAuth/QOAuth1Signature-c.rst

    .. sip:enum:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod
        :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-e.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Custom
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Custom-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Delete
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Delete-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Get
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Get-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Head
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Head-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Post
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Post-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Put
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Put-v.rst

        .. sip:enum-member:: PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Unknown
            :description: QtNetworkAuth/QOAuth1Signature-HttpRequestMethod-Unknown-v.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature`
        :description: QtNetworkAuth/QOAuth1Signature-__init__-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.__init__
        :args:
            url: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
            method: :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod` = :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Post`
            parameters: unknown-type = {}
        :description: QtNetworkAuth/QOAuth1Signature-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            str
            str
            method: :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod` = :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod.Post`
            parameters: unknown-type = {}
        :description: QtNetworkAuth/QOAuth1Signature-__init__-f-2.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.addRequestBody
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrlQuery`
        :description: QtNetworkAuth/QOAuth1Signature-addRequestBody-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.clientSharedKey
        :returns:
            str
        :description: QtNetworkAuth/QOAuth1Signature-clientSharedKey-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.customMethodString
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetworkAuth/QOAuth1Signature-customMethodString-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.hmacSha1
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetworkAuth/QOAuth1Signature-hmacSha1-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.httpRequestMethod
        :returns:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod`
        :description: QtNetworkAuth/QOAuth1Signature-httpRequestMethod-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.insert
        :args:
            str
            Any
        :description: QtNetworkAuth/QOAuth1Signature-insert-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.keys
        :returns:
            List[str]
        :description: QtNetworkAuth/QOAuth1Signature-keys-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.parameters
        :returns:
            Dict[str, List[Any]]
        :description: QtNetworkAuth/QOAuth1Signature-parameters-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.plainText
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetworkAuth/QOAuth1Signature-plainText-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.plainText
        :args:
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtNetworkAuth/QOAuth1Signature-plainText-f-1.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.rsaSha1
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetworkAuth/QOAuth1Signature-rsaSha1-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.setClientSharedKey
        :args:
            str
        :description: QtNetworkAuth/QOAuth1Signature-setClientSharedKey-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.setCustomMethodString
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetworkAuth/QOAuth1Signature-setCustomMethodString-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.setHttpRequestMethod
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod`
        :description: QtNetworkAuth/QOAuth1Signature-setHttpRequestMethod-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.setParameters
        :args:
            unknown-type
        :description: QtNetworkAuth/QOAuth1Signature-setParameters-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.setTokenSecret
        :args:
            str
        :description: QtNetworkAuth/QOAuth1Signature-setTokenSecret-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.setUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1Signature-setUrl-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.swap
        :args:
            :sip:ref:`~PyQt6.QtNetworkAuth.QOAuth1Signature`
        :description: QtNetworkAuth/QOAuth1Signature-swap-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.take
        :args:
            str
        :returns:
            Any
        :description: QtNetworkAuth/QOAuth1Signature-take-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.tokenSecret
        :returns:
            str
        :description: QtNetworkAuth/QOAuth1Signature-tokenSecret-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.url
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetworkAuth/QOAuth1Signature-url-f.rst

    .. sip:method:: PyQt6.QtNetworkAuth.QOAuth1Signature.value
        :args:
            str
            defaultValue: Any = None
        :returns:
            Any
        :description: QtNetworkAuth/QOAuth1Signature-value-f.rst
