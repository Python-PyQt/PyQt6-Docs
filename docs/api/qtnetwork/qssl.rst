:orphan:

.. sip:class:: PyQt6.QtNetwork.QSsl
    :description: QtNetwork/QSsl-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.AlertLevel
        :description: QtNetwork/QSsl-AlertLevel-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertLevel.Fatal
            :description: QtNetwork/QSsl-AlertLevel-Fatal-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertLevel.Unknown
            :description: QtNetwork/QSsl-AlertLevel-Unknown-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertLevel.Warning
            :description: QtNetwork/QSsl-AlertLevel-Warning-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.AlertType
        :description: QtNetwork/QSsl-AlertType-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.AccessDenied
            :description: QtNetwork/QSsl-AlertType-AccessDenied-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.BadCertificate
            :description: QtNetwork/QSsl-AlertType-BadCertificate-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.BadCertificateHashValue
            :description: QtNetwork/QSsl-AlertType-BadCertificateHashValue-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.BadCertificateStatusResponse
            :description: QtNetwork/QSsl-AlertType-BadCertificateStatusResponse-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.BadRecordMac
            :description: QtNetwork/QSsl-AlertType-BadRecordMac-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.CertificateExpired
            :description: QtNetwork/QSsl-AlertType-CertificateExpired-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.CertificateRequired
            :description: QtNetwork/QSsl-AlertType-CertificateRequired-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.CertificateRevoked
            :description: QtNetwork/QSsl-AlertType-CertificateRevoked-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.CertificateUnknown
            :description: QtNetwork/QSsl-AlertType-CertificateUnknown-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.CertificateUnobtainable
            :description: QtNetwork/QSsl-AlertType-CertificateUnobtainable-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.CloseNotify
            :description: QtNetwork/QSsl-AlertType-CloseNotify-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.DecodeError
            :description: QtNetwork/QSsl-AlertType-DecodeError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.DecompressionFailure
            :description: QtNetwork/QSsl-AlertType-DecompressionFailure-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.DecryptError
            :description: QtNetwork/QSsl-AlertType-DecryptError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.ExportRestriction
            :description: QtNetwork/QSsl-AlertType-ExportRestriction-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.HandshakeFailure
            :description: QtNetwork/QSsl-AlertType-HandshakeFailure-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.IllegalParameter
            :description: QtNetwork/QSsl-AlertType-IllegalParameter-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.InappropriateFallback
            :description: QtNetwork/QSsl-AlertType-InappropriateFallback-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.InsufficientSecurity
            :description: QtNetwork/QSsl-AlertType-InsufficientSecurity-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.InternalError
            :description: QtNetwork/QSsl-AlertType-InternalError-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.MissingExtension
            :description: QtNetwork/QSsl-AlertType-MissingExtension-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.NoApplicationProtocol
            :description: QtNetwork/QSsl-AlertType-NoApplicationProtocol-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.NoCertificate
            :description: QtNetwork/QSsl-AlertType-NoCertificate-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.NoRenegotiation
            :description: QtNetwork/QSsl-AlertType-NoRenegotiation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.ProtocolVersion
            :description: QtNetwork/QSsl-AlertType-ProtocolVersion-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.RecordOverflow
            :description: QtNetwork/QSsl-AlertType-RecordOverflow-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnexpectedMessage
            :description: QtNetwork/QSsl-AlertType-UnexpectedMessage-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnknownAlertMessage
            :description: QtNetwork/QSsl-AlertType-UnknownAlertMessage-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnknownCa
            :description: QtNetwork/QSsl-AlertType-UnknownCa-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnknownPskIdentity
            :description: QtNetwork/QSsl-AlertType-UnknownPskIdentity-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnrecognizedName
            :description: QtNetwork/QSsl-AlertType-UnrecognizedName-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnsupportedCertificate
            :description: QtNetwork/QSsl-AlertType-UnsupportedCertificate-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UnsupportedExtension
            :description: QtNetwork/QSsl-AlertType-UnsupportedExtension-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlertType.UserCancelled
            :description: QtNetwork/QSsl-AlertType-UserCancelled-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.AlternativeNameEntryType
        :description: QtNetwork/QSsl-AlternativeNameEntryType-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlternativeNameEntryType.DnsEntry
            :description: QtNetwork/QSsl-AlternativeNameEntryType-DnsEntry-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlternativeNameEntryType.EmailEntry
            :description: QtNetwork/QSsl-AlternativeNameEntryType-EmailEntry-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.AlternativeNameEntryType.IpAddressEntry
            :description: QtNetwork/QSsl-AlternativeNameEntryType-IpAddressEntry-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.EncodingFormat
        :description: QtNetwork/QSsl-EncodingFormat-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.EncodingFormat.Der
            :description: QtNetwork/QSsl-EncodingFormat-Der-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.EncodingFormat.Pem
            :description: QtNetwork/QSsl-EncodingFormat-Pem-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.KeyAlgorithm
        :description: QtNetwork/QSsl-KeyAlgorithm-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyAlgorithm.Dh
            :description: QtNetwork/QSsl-KeyAlgorithm-Dh-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyAlgorithm.Dsa
            :description: QtNetwork/QSsl-KeyAlgorithm-Dsa-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyAlgorithm.Ec
            :description: QtNetwork/QSsl-KeyAlgorithm-Ec-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyAlgorithm.Opaque
            :description: QtNetwork/QSsl-KeyAlgorithm-Opaque-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyAlgorithm.Rsa
            :description: QtNetwork/QSsl-KeyAlgorithm-Rsa-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.KeyType
        :description: QtNetwork/QSsl-KeyType-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyType.PrivateKey
            :description: QtNetwork/QSsl-KeyType-PrivateKey-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.KeyType.PublicKey
            :description: QtNetwork/QSsl-KeyType-PublicKey-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.SslOptions
        :description: QtNetwork/QSsl-SslOptions-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableCompression
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableCompression-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableEmptyFragments
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableEmptyFragments-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableLegacyRenegotiation
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableLegacyRenegotiation-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableServerCipherPreference
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableServerCipherPreference-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableServerNameIndication
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableServerNameIndication-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionPersistence
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableSessionPersistence-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionSharing
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableSessionSharing-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslOptions.SslOptionDisableSessionTickets
            :description: QtNetwork/QSsl-SslOptions-SslOptionDisableSessionTickets-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSsl.SslProtocol
        :description: QtNetwork/QSsl-SslProtocol-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.AnyProtocol
            :description: QtNetwork/QSsl-SslProtocol-AnyProtocol-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.DtlsV1_0
            :description: QtNetwork/QSsl-SslProtocol-DtlsV1_0-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.DtlsV1_0OrLater
            :description: QtNetwork/QSsl-SslProtocol-DtlsV1_0OrLater-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.DtlsV1_2
            :description: QtNetwork/QSsl-SslProtocol-DtlsV1_2-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.DtlsV1_2OrLater
            :description: QtNetwork/QSsl-SslProtocol-DtlsV1_2OrLater-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.SecureProtocols
            :description: QtNetwork/QSsl-SslProtocol-SecureProtocols-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_0
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_0-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_0OrLater
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_0OrLater-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_1
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_1-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_1OrLater
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_1OrLater-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_2
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_2-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_2OrLater
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_2OrLater-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_3
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_3-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.TlsV1_3OrLater
            :description: QtNetwork/QSsl-SslProtocol-TlsV1_3OrLater-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSsl.SslProtocol.UnknownProtocol
            :description: QtNetwork/QSsl-SslProtocol-UnknownProtocol-v.rst
