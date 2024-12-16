.. sip:method-description::
    :status: todo
    :pysig: 782079b28f70742734bbb559f9c5fba0
    :realsig: () const
    :digest: 583d0b8247a89c5e23b8de23e22c7b5d

Returns the list of TLS association records associated with this lookup.

According to the standards relating to DNS-based Authentication of Named Entities (DANE), this field should be ignored and must not be used for verifying the authentity of a given server if the authenticity of the DNS reply cannot itself be confirmed. See :sip:ref:`~PyQt6.QtNetwork.QDnsLookup.isAuthenticData` for more information.
