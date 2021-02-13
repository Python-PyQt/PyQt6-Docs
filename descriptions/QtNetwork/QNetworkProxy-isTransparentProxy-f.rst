.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 07fccdd3a816fb2f006e05a049aba8a2

Returns ``true`` if this proxy supports transparent tunneling of TCP connections. This matches the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.Capabilities.TunnelingCapability` capability.

In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5 it is possible to remove the capability of caching from a proxy by calling :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setCapabilities`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.capabilities`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.type`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.isCachingProxy`.
