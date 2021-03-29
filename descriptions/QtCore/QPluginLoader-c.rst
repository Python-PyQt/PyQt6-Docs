.. sip:class-description::
    :status: todo
    :brief: Loads a plugin at run-time
    :digest: 81d2da9d0b7d9e9d0744c487d184d57f

The :sip:ref:`~PyQt6.QtCore.QPluginLoader` class loads a plugin at run-time.

:sip:ref:`~PyQt6.QtCore.QPluginLoader` provides access to a Qt plugin. A Qt plugin is stored in a shared library (a DLL) and offers these benefits over shared libraries accessed using :sip:ref:`~PyQt6.QtCore.QLibrary`:

* :sip:ref:`~PyQt6.QtCore.QPluginLoader` checks that a plugin is linked against the same version of Qt as the application.

* :sip:ref:`~PyQt6.QtCore.QPluginLoader` provides direct access to a root component object (\ :sip:ref:`~PyQt6.QtCore.QPluginLoader.instance`), instead of forcing you to resolve a C function manually.

An instance of a :sip:ref:`~PyQt6.QtCore.QPluginLoader` object operates on a single shared library file, which we call a plugin. It provides access to the functionality in the plugin in a platform-independent way. To specify which plugin to load, either pass a file name in the constructor or set it with :sip:ref:`~PyQt6.QtCore.QPluginLoader.setFileName`.

The most important functions are :sip:ref:`~PyQt6.QtCore.QPluginLoader.load` to dynamically load the plugin file, :sip:ref:`~PyQt6.QtCore.QPluginLoader.isLoaded` to check whether loading was successful, and :sip:ref:`~PyQt6.QtCore.QPluginLoader.instance` to access the root component in the plugin. The :sip:ref:`~PyQt6.QtCore.QPluginLoader.instance` function implicitly tries to load the plugin if it has not been loaded yet. Multiple instances of :sip:ref:`~PyQt6.QtCore.QPluginLoader` can be used to access the same physical plugin.

Once loaded, plugins remain in memory until all instances of :sip:ref:`~PyQt6.QtCore.QPluginLoader` has been unloaded, or until the application terminates. You can attempt to unload a plugin using :sip:ref:`~PyQt6.QtCore.QPluginLoader.unload`, but if other instances of :sip:ref:`~PyQt6.QtCore.QPluginLoader` are using the same library, the call will fail, and unloading will only happen when every instance has called :sip:ref:`~PyQt6.QtCore.QPluginLoader.unload`. Right before the unloading happens, the root component will also be deleted.

See How to Create Qt Plugins for more information about how to make your application extensible through plugins.

Note that the :sip:ref:`~PyQt6.QtCore.QPluginLoader` cannot be used if your application is statically linked against Qt. In this case, you will also have to link to plugins statically. You can use :sip:ref:`~PyQt6.QtCore.QLibrary` if you need to load dynamic libraries in a statically linked application.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary`, `Plug & Paint Example <https://doc.qt.io/qt-6/qtwidgets-tools-plugandpaint-app-example.html>`_.
