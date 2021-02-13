.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 15fc1977fc36cf6ceae6197ded24531d

Returns a name that describes the issuer. It returns the :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo.CommonName` if available, otherwise falls back to the first :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo.Organization` or the first :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.SubjectInfo.OrganizationalUnitName`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.issuerInfo`.
