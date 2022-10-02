.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: af40d1ff2a0730671c0388d3bf487c0e

Unloads the plugin and returns ``true`` if the plugin could be unloaded; otherwise returns ``false``.

This happens automatically on application termination, so you shouldn't normally need to call this function.

If other instances of :sip:ref:`~PyQt6.QtCore.QPluginLoader` are using the same plugin, the call will fail, and unloading will only happen when every instance has called unload().

Don't try to delete the root component. Instead rely on that unload() will automatically delete it when needed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPluginLoader.instance`, :sip:ref:`~PyQt6.QtCore.QPluginLoader.load`.
