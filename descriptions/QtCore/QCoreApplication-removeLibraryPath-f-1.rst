.. sip:method-description::
    :status: todo
    :pysig: c5283bf81cad04335531dd6931c2734d
    :realsig: (const QString&)
    :digest: 0a38a2012299a646b87ecd97f31cbeb2

Removes *path* from the library path list. If *path* is empty or not in the path list, the list is not changed.

The library paths are reset to the default when an instance of :sip:ref:`~PyQt6.QtCore.QCoreApplication` is destructed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.addLibraryPath`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.libraryPaths`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.setLibraryPaths`.
