.. sip:method-description::
    :status: todo
    :pysig: be6eed7db3c6e9da81b7b87e9761d4dc
    :realsig: (const QWebEngineExtensionInfo&)
    :digest: d97efde1e627cceae3f5abed6bf8619f

Unloads the *extension*

Removes all the extension's data from memory.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.unloadFinished` signal is emitted after the unload process finished.

**Note:** It is also possible to unload internal extensions like Hangouts and PDF, but they will be loaded at next startup like other installed extensions.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo.isLoaded`.
