.. sip:class-description::
    :status: todo
    :brief: Information about a browser extension
    :digest: bced3fcbcfc15812cf96dc9380a1894d

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo` provides information about a browser extension.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo` provides information of an extension loaded into Qt WebEngine. Extensions can be loaded via the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager`. You can check if the extension was successfully loaded using its :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isLoaded` property. The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.error` property contains error messages if the loading process failed. Extensions are always loaded in disabled state. To run an extension, it has to be enabled via :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.setExtensionEnabled`.

An extension can be removed using :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.unloadExtension`.

You can access extensions with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.extensions` which provides a list of the loaded extensions, or connect to the manager's signals to be notified if the loading process is complete.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.extensionManager`.
