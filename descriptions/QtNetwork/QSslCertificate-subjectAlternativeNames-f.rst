.. sip:method-description::
    :status: todo
    :pysig: 259fbe8981b063c33fa82e896b3f1fa4
    :realsig: () const
    :digest: 5679e68c6a1d03b4d9d55aa37253c841

Returns the list of alternative subject names for this certificate. The alternative names typically contain host names, optionally with wildcards, that are valid for this certificate.

These names are tested against the connected peer's host name, if either the subject information for :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo.CommonName` doesn't define a valid host name, or the subject info name doesn't match the peer's host name.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.subjectInfo`.
