.. sip:method-description::
    :status: todo
    :pysig: e0b286fa9e7df2ac0cd416991cb594d8
    :realsig: (const QNetworkProxy&)
    :digest: e89c1fedb03328ceec713526085bc34e

Sets the application level network proxying to be *networkProxy*.

If a :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` or :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` has the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.DefaultProxy` type, then the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy` set with this function is used. If you want more flexibility in determining which proxy is used, use the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory` class.

Setting a default proxy value with this function will override the application proxy factory set with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.setApplicationProxyFactory`, and disable the use of a system proxy.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.applicationProxy`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setProxy`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer.setProxy`.
