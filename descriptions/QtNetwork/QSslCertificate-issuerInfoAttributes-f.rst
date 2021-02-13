.. sip:method-description::
    :status: todo
    :pysig: 3d58b35510c8def711868c852c1c5630
    :realsig: () const
    :digest: 333c81c0fc38177609ad217a5511c377

Returns a list of the attributes that have values in the issuer information of this certificate. The information associated with a given attribute can be accessed using the :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.issuerInfo` method. Note that this list may include the OIDs for any elements that are not known by the SSL backend.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.subjectInfo`.
