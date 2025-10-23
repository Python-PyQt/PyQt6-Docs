.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: f3e103299ecd2a8d3fed52ecaa4f204d

Installs an extension from *path* to the profile's directory and loads it

The QWebEngineExtensionManager::installFinished signal is emitted after an extension is installed or the install failed. If the install succeeded :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isInstalled` will return true, otherwise :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.error` will contain information how the install process failed.

Extensions are loaded in disabled state after the install succeded. Installed extensions are automatically loaded at every starutup in disabled state. The install path can be queried with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.installPath`.

The installer is capable of installing zipped or unpacked extensions. The *path* parameter should point to a directory or a zip file containing the extension's manifest file. If the manifest is missing from the top level directory, the install process will abort.

Installing an already loaded or installed extension from the same path will install a new extension.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isInstalled`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.error`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.installPath`.
