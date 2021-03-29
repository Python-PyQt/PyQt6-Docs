.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 3eb2ff9f10e806b2a0c318c3b625e5c5

Returns ``true`` if this cookie is a session cookie. A session cookie is a cookie which has no expiration date, which means it should be discarded when the application's concept of session is over (usually, when the application exits).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.expirationDate`, :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.setExpirationDate`.
