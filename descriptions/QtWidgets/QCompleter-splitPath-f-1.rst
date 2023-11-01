.. sip:method-description::
    :status: todo
    :pysig: dfde435543c36ef0c5a850595dd5804d
    :realsig: (const QString&) const
    :digest: 518ee4a72311afe833138eb8d9c6e8a5

Splits the given *path* into strings that are used to match at each level in the :sip:ref:`~PyQt6.QtWidgets.QCompleter.model`.

The default implementation of splitPath() splits a file system path based on :sip:ref:`~PyQt6.QtCore.QDir.separator` when the sourceModel() is a :sip:ref:`~PyQt6.QtGui.QFileSystemModel`.

When used with list models, the first item in the returned list is used for matching.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.pathFromIndex`, :ref:`qcompleter-handling-tree-models`.
