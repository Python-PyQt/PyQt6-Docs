.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 2387c9ffa2410bd098a79ffd5419b099

Prepends *path* to the beginning of the library path list, ensuring that it is searched for libraries first. If *path* is empty or already in the path list, the path list is not changed.

The default path list consists of a single entry, the installation directory for plugins. The default installation directory for plugins is ``INSTALL/plugins``, where ``INSTALL`` is the directory where Qt was installed.

The library paths are reset to the default when an instance of :sip:ref:`~PyQt6.QtCore.QCoreApplication` is destructed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.removeLibraryPath`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.libraryPaths`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.setLibraryPaths`.
