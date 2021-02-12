.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: ()
    :digest: bc0c3a32af58e66a8c1b6df7bc19fc44

Returns the root component object of the plugin. The plugin is loaded if necessary. The function returns ``nullptr`` if the plugin could not be loaded or if the root component object could not be instantiated.

If the root component object was destroyed, calling this function creates a new instance.

The root component, returned by this function, is not deleted when the :sip:ref:`~PyQt6.QtCore.QPluginLoader` is destroyed. If you want to ensure that the root component is deleted, you should call :sip:ref:`~PyQt6.QtCore.QPluginLoader.unload` as soon you don't need to access the core component anymore. When the library is finally unloaded, the root component will automatically be deleted.

The component object is a :sip:ref:`~PyQt6.QtCore.QObject`. Use qobject_cast() to access interfaces you are interested in.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPluginLoader.load`.
