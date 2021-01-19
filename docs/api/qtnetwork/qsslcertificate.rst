:orphan:

.. sip:class:: PyQt6.QtNetwork.QSslCertificate
    :description: QtNetwork/QSslCertificate-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QSslCertificate.PatternSyntax
        :description: QtNetwork/QSslCertificate-PatternSyntax-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.PatternSyntax.FixedString
            :description: QtNetwork/QSslCertificate-PatternSyntax-FixedString-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.PatternSyntax.RegularExpression
            :description: QtNetwork/QSslCertificate-PatternSyntax-RegularExpression-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.PatternSyntax.Wildcard
            :description: QtNetwork/QSslCertificate-PatternSyntax-Wildcard-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo
        :description: QtNetwork/QSslCertificate-SubjectInfo-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.CommonName
            :description: QtNetwork/QSslCertificate-SubjectInfo-CommonName-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.CountryName
            :description: QtNetwork/QSslCertificate-SubjectInfo-CountryName-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.DistinguishedNameQualifier
            :description: QtNetwork/QSslCertificate-SubjectInfo-DistinguishedNameQualifier-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.EmailAddress
            :description: QtNetwork/QSslCertificate-SubjectInfo-EmailAddress-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.LocalityName
            :description: QtNetwork/QSslCertificate-SubjectInfo-LocalityName-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.Organization
            :description: QtNetwork/QSslCertificate-SubjectInfo-Organization-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.OrganizationalUnitName
            :description: QtNetwork/QSslCertificate-SubjectInfo-OrganizationalUnitName-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.SerialNumber
            :description: QtNetwork/QSslCertificate-SubjectInfo-SerialNumber-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QSslCertificate.SubjectInfo.StateOrProvinceName
            :description: QtNetwork/QSslCertificate-SubjectInfo-StateOrProvinceName-v.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslCertificate-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
        :description: QtNetwork/QSslCertificate-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.__init__
        :args:
            data: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
        :description: QtNetwork/QSslCertificate-__init__-f-2.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.clear
        :description: QtNetwork/QSslCertificate-clear-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.digest
        :args:
            algorithm: :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm` = :sip:ref:`~PyQt6.QtCore.QCryptographicHash.Algorithm.Md5`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslCertificate-digest-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.effectiveDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtNetwork/QSslCertificate-effectiveDate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.__eq__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :returns:
            bool
        :description: QtNetwork/QSslCertificate-__eq__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.expiryDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtNetwork/QSslCertificate-expiryDate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.extensions
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificateExtension`]
        :description: QtNetwork/QSslCertificate-extensions-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.fromData
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :static:
        :description: QtNetwork/QSslCertificate-fromData-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.fromDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :static:
        :description: QtNetwork/QSslCertificate-fromDevice-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.fromPath
        :args:
            str
            format: :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat` = :sip:ref:`~PyQt6.QtNetwork.QSsl.EncodingFormat.Pem`
            syntax: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.PatternSyntax` = :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.PatternSyntax.FixedString`
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
        :static:
        :description: QtNetwork/QSslCertificate-fromPath-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.handle
        :returns:
            sip.voidptr
        :description: QtNetwork/QSslCertificate-handle-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.__hash__
        :returns:
            int
        :description: QtNetwork/QSslCertificate-__hash__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.importPkcs12
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
            caCertificates: Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`] = []
            passPhrase: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
        :returns:
            bool
        :static:
        :description: QtNetwork/QSslCertificate-importPkcs12-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.isBlacklisted
        :returns:
            bool
        :description: QtNetwork/QSslCertificate-isBlacklisted-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.isNull
        :returns:
            bool
        :description: QtNetwork/QSslCertificate-isNull-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.isSelfSigned
        :returns:
            bool
        :description: QtNetwork/QSslCertificate-isSelfSigned-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.issuerDisplayName
        :returns:
            str
        :description: QtNetwork/QSslCertificate-issuerDisplayName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.issuerInfo
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo`
        :returns:
            List[str]
        :description: QtNetwork/QSslCertificate-issuerInfo-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.issuerInfo
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            List[str]
        :description: QtNetwork/QSslCertificate-issuerInfo-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.issuerInfoAttributes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetwork/QSslCertificate-issuerInfoAttributes-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.__ne__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :returns:
            bool
        :description: QtNetwork/QSslCertificate-__ne__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.publicKey
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QSslKey`
        :description: QtNetwork/QSslCertificate-publicKey-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.serialNumber
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslCertificate-serialNumber-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.subjectAlternativeNames
        :returns:
            Dict[:sip:ref:`~PyQt6.QtNetwork.QSsl.AlternativeNameEntryType`, List[str]]
        :description: QtNetwork/QSslCertificate-subjectAlternativeNames-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.subjectDisplayName
        :returns:
            str
        :description: QtNetwork/QSslCertificate-subjectDisplayName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.subjectInfo
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo`
        :returns:
            List[str]
        :description: QtNetwork/QSslCertificate-subjectInfo-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.subjectInfo
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            List[str]
        :description: QtNetwork/QSslCertificate-subjectInfo-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.subjectInfoAttributes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtNetwork/QSslCertificate-subjectInfoAttributes-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`
        :description: QtNetwork/QSslCertificate-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.toDer
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslCertificate-toDer-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.toPem
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslCertificate-toPem-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.toText
        :returns:
            str
        :description: QtNetwork/QSslCertificate-toText-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.verify
        :args:
            Iterable[:sip:ref:`~PyQt6.QtNetwork.QSslCertificate`]
            hostName: str = ''
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QSslError`]
        :static:
        :description: QtNetwork/QSslCertificate-verify-f.rst

    .. sip:method:: PyQt6.QtNetwork.QSslCertificate.version
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QSslCertificate-version-f.rst
