.. sip:class-description::
    :status: todo
    :brief: Allows applications to install and load Chrome extensions from the filesystem
    :digest: 4c781e37ed89cebe777d08bfeab90eab

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager` class allows applications to install and load Chrome extensions from the filesystem.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager` can load or install Chrome extensions. Extensions can be loaded via :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.loadExtension`. Extensions loaded this way are not remembered by the associated profile and has to be manually loaded in every new browsing session. To preserve extensions between browsing sessions, applications can install zipped or unpacked extensions via :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.installExtension`. In this case the manager will unpack the extension to the profile's directory and load it from there. Installed extensions are always loaded at startup, after the profile is initialized.

You can access the loaded extensions with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager.extensions` which provides a list of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo`, or connect to the manager's signals to get notified about the state of the load or install processes.

Each :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` has its own :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionManager`, so every page that shares the same profile will share the same extensions too. Extensions can't be loaded into off-the-record profiles.

**Note:** Only ManifestV3 extensions are supported, other versions won't be loaded nor installed

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.extensionManager`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineExtensionInfo`.
