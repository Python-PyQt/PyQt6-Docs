.. sip:method-description::
    :status: todo
    :pysig: 91a36dfa64d1bc692750bce88a36572d
    :realsig: (const QStringList&)
    :digest: cf5ef452692376758f67fa3dff3c8b4f

Sets the list of directories to search when loading plugins with :sip:ref:`~PyQt6.QtCore.QLibrary` to *paths*. All existing paths will be deleted and the path list will consist of the paths given in *paths* and the path to the application.

The library paths are reset to the default when an instance of :sip:ref:`~PyQt6.QtCore.QCoreApplication` is destructed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.libraryPaths`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.addLibraryPath`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.removeLibraryPath`, :sip:ref:`~PyQt6.QtCore.QLibrary`.
