.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: bfac764cff6570f36089ac47c07c5676

Returns ``true`` if the "HttpOnly" flag is enabled for this cookie.

A cookie that is "HttpOnly" is only set and retrieved by the network requests and replies; i.e., the HTTP protocol. It is not accessible from scripts running on browsers.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.isSecure`.
