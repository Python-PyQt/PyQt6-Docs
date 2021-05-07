.. sip:method-description::
    :status: todo
    :pysig: 0cd9e09957ea12b1d27b829d8b368462
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: 47aa5b24c5189ffe5436e8fa7077df9d

Returns the host of the URL if it is defined; otherwise an empty string is returned.

The *options* argument controls how the hostname will be formatted. The :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.EncodeUnicode` option will cause this function to return the hostname in the ASCII-Compatible Encoding (ACE) form, which is suitable for use in channels that are not 8-bit clean or that require the legacy hostname (such as DNS requests or in HTTP request headers). If that flag is not present, this function returns the International Domain Name (IDN) in Unicode form, according to the list of permissible top-level domains (see :sip:ref:`~PyQt6.QtCore.QUrl.idnWhitelist`).

All other flags are ignored. Host names cannot contain control or percent characters, so the returned value can be considered fully decoded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setHost`, :sip:ref:`~PyQt6.QtCore.QUrl.idnWhitelist`, :sip:ref:`~PyQt6.QtCore.QUrl.setIdnWhitelist`, :sip:ref:`~PyQt6.QtCore.QUrl.authority`.
