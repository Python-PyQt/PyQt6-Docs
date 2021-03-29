.. sip:method-description::
    :status: todo
    :pysig: 763826b9ddee7d38af68244256ffe244
    :realsig: (QNetworkCookie::RawForm) const
    :digest: f1ab2c2458636f27deda5c91a97c0a18

Returns the raw form of this :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`. The :sip:ref:`~PyQt6.QtCore.QByteArray` returned by this function is suitable for an HTTP header, either in a server response (the Set-Cookie header) or the client request (the Cookie header). You can choose from one of two formats, using *form*.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.parseCookies`.
