.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 70d7e61e0363c6d3083ae9f90ee45c78

Returns ``true`` if the "secure" option was specified in the cookie string, false otherwise.

Secure cookies may contain private information and should not be resent over unencrypted connections.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.setSecure`.
