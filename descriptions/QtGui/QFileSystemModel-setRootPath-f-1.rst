.. sip:method-description::
    :status: todo
    :pysig: 52d11af17f0321c2fb9ec14a69771a6e
    :realsig: (const QString&)
    :digest: e2f51557e295a9abf1fb429418c4c82d

Sets the directory that is being watched by the model to *newPath* by installing a :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher` on it. Any changes to files and directories within this directory will be reflected in the model.

If the path is changed, the :sip:ref:`~PyQt6.QtGui.QFileSystemModel.rootPathChanged` signal will be emitted.

**Note:** This function does not change the structure of the model or modify the data available to views. In other words, the "root" of the model is *not* changed to include only files and directories within the directory specified by *newPath* in the file system.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFileSystemModel.rootPath`.
