.. sip:method-description::
    :status: todo
    :pysig: be6eed7db3c6e9da81b7b87e9761d4dc
    :realsig: (const QWebEngineExtensionInfo&)
    :digest: 0428c3ab2a9a2b6f11346a76debab3ce

Unloads the *extension*

Removes all the extension's data from memory.

The QWebEngineExtensionManager::unloadFinished signal is emitted after the unload process finished.

**Note:** It is also possible to unload internal extensions like Hangouts and PDF, but they will be loaded at next startup like other installed extensions.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isLoaded`.
