.. sip:method-description::
    :status: todo
    :pysig: 3ccdc05659b897ae06670c52d6ea0937
    :realsig: (const QStringList&)
    :digest: ebf59a1cd9943172eaf167453ca19c55

Removes the specified *paths* from the file system watcher.

The return value is a list of paths which were not able to be unwatched successfully.

Reasons for watch removal failing are generally system-dependent, but may be due to the path having already been deleted, for example.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePath`, :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPaths`.
