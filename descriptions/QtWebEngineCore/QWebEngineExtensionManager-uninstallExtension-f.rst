.. sip:method-description::
    :status: todo
    :pysig: be6eed7db3c6e9da81b7b87e9761d4dc
    :realsig: (const QWebEngineExtensionInfo&)
    :digest: 520e6bc3a66a749e215e68eb5a519dcb

Uninstalls the *extension*

Removes the extension's files from the install path and unloads the extension. The QWebEngineExtensionManager::uninstallFinished signal is emitted after the process finished.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.installPath`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isInstalled`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.error`.
