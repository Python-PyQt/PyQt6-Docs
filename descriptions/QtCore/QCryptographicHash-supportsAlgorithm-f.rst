.. sip:method-description::
    :status: todo
    :pysig: 0520dad70da53e115d0f1e8560543e81
    :realsig: (QCryptographicHash::Algorithm)
    :digest: 4515e563d3a95202f3ecf4caea20cc58

Returns whether the selected algorithm *method* is supported and if :sip:ref:`~PyQt6.QtCore.QCryptographicHash.result` will return a value when the *method* is used.

**Note:** OpenSSL will be responsible for providing this information when used as a provider, otherwise ``true`` will be returned as the non-OpenSSL implementation doesn't have any restrictions. We return ``false`` if we fail to query OpenSSL.
