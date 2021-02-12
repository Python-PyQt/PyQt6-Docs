.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: c5b535050ce61a0a4215238c84499a33

Loads the plugin and returns ``true`` if the plugin was loaded successfully; otherwise returns ``false``. Since :sip:ref:`~PyQt6.QtCore.QPluginLoader.instance` always calls this function before resolving any symbols it is not necessary to call it explicitly. In some situations you might want the plugin loaded in advance, in which case you would use this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPluginLoader.unload`.
