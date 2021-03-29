.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 543d0eaf155bb05d380377aa99faa483

Returns ``true`` if this proxy supports the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.Capabilities.CachingCapability` capability.

In Qt 4.4, the capability was tied to the proxy type, but since Qt 4.5 it is possible to remove the capability of caching from a proxy by calling :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setCapabilities`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.capabilities`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.type`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.isTransparentProxy`.
