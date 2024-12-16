.. sip:method-description::
    :status: todo
    :pysig: 44749fd150362d078dc16c6fe99ad605
    :realsig: (const QString&) const
    :digest: 518ee4a72311afe833138eb8d9c6e8a5

Splits the given *path* into strings that are used to match at each level in the :sip:ref:`~PyQt6.QtWidgets.QCompleter.model`.

The default implementation of splitPath() splits a file system path based on :sip:ref:`~PyQt6.QtCore.QDir.separator` when the sourceModel() is a :sip:ref:`~PyQt6.QtGui.QFileSystemModel`.

When used with list models, the first item in the returned list is used for matching.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.pathFromIndex`, :ref:`qcompleter-handling-tree-models`.
