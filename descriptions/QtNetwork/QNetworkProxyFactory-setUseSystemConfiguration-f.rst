.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: (bool)
    :digest: 7cb391f3fff70ee76174e4bc7c8d4896

Enables the use of the platform-specific proxy settings, and only those. See :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.systemProxyForQuery` for more information.

Calling this function with *enable* set to ``true`` resets any proxy or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory` that is already set.

**Note:** See the :sip:ref:`~PyQt6.QtNetwork.QNetworkProxyFactory.systemProxyForQuery` documentation for a list of limitations related to the use of system proxies.
