.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 91f333c001fafaa2c2b982b7fb7fc4af

Loads an unpacked extension from *path*

The QWebEngineExtensionManager::loadFinished signal is emitted when an extension is loaded or the load failed. If the load succeeded :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isLoaded` will return true otherwise :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.error` will contain information where the loading process failed.

Extensions are always loaded in disabled state, users have to enable them manually. Loading an already loaded extension from the same path will reload the extension.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isLoaded`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.error`.
