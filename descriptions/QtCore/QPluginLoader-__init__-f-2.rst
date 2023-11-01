.. sip:method-description::
    :status: todo
    :pysig: 7d74642492c1254c6ab51fbfe503f7bc
    :realsig: (const QString&, QObject*)
    :digest: e6b8020e4e249c2c584d6d2c80d75721

Constructs a plugin loader with the given *parent* that will load the plugin specified by *fileName*.

To be loadable, the file's suffix must be a valid suffix for a loadable library in accordance with the platform, e.g. ``.so`` on Unix, - ``.dylib`` on macOS and iOS, and ``.dll`` on Windows. The suffix can be verified with :sip:ref:`~PyQt6.QtCore.QLibrary.isLibrary`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPluginLoader.setFileName`.
