.. sip:method-description::
    :status: todo
    :pysig: 32e5fb7304ae5e1f9fdeb0568741dd17
    :realsig: () const
    :digest: 5679e68c6a1d03b4d9d55aa37253c841

Returns the list of alternative subject names for this certificate. The alternative names typically contain host names, optionally with wildcards, that are valid for this certificate.

These names are tested against the connected peer's host name, if either the subject information for :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo.CommonName` doesn't define a valid host name, or the subject info name doesn't match the peer's host name.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.subjectInfo`.
