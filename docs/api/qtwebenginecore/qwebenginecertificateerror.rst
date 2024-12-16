:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineCertificateError
    :description: QtWebEngineCore/QWebEngineCertificateError-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type
        :description: QtWebEngineCore/QWebEngineCertificateError-Type-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateAuthorityInvalid
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateAuthorityInvalid-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateCommonNameInvalid
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateCommonNameInvalid-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateContainsErrors
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateContainsErrors-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateDateInvalid
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateDateInvalid-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateInvalid
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateInvalid-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateKnownInterceptionBlocked
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateKnownInterceptionBlocked-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateNameConstraintViolation
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateNameConstraintViolation-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateNonUniqueName
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateNonUniqueName-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateNoRevocationMechanism
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateNoRevocationMechanism-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateRevoked
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateRevoked-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateSymantecLegacy
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateSymantecLegacy-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateTransparencyRequired
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateTransparencyRequired-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateUnableToCheckRevocation
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateUnableToCheckRevocation-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateValidityTooLong
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateValidityTooLong-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateWeakKey
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateWeakKey-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.CertificateWeakSignatureAlgorithm
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-CertificateWeakSignatureAlgorithm-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.SslObsoleteVersion
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-SslObsoleteVersion-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type.SslPinnedKeyNotInCertificateChain
            :description: QtWebEngineCore/QWebEngineCertificateError-Type-SslPinnedKeyNotInCertificateChain-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.__init__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCertificateError`
        :description: QtWebEngineCore/QWebEngineCertificateError-__init__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.acceptCertificate
        :description: QtWebEngineCore/QWebEngineCertificateError-acceptCertificate-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.certificateChain
        :returns:
            list[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :description: QtWebEngineCore/QWebEngineCertificateError-certificateChain-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.defer
        :description: QtWebEngineCore/QWebEngineCertificateError-defer-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.description
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineCertificateError-description-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.isMainFrame
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineCertificateError-isMainFrame-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.isOverridable
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineCertificateError-isOverridable-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.rejectCertificate
        :description: QtWebEngineCore/QWebEngineCertificateError-rejectCertificate-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.type
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineCertificateError.Type`
        :description: QtWebEngineCore/QWebEngineCertificateError-type-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineCertificateError.url
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineCertificateError-url-f.rst
