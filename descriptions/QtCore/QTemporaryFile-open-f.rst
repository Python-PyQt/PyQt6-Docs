.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: a93240dae45f40b92719c6ed082c1bd8

Opens a unique temporary file in the file system in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite` mode. Returns ``true`` if the file was successfully opened, or was already open. Otherwise returns ``false``.

If called for the first time, open() will create a unique file name based on :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`. The file is guaranteed to have been created by this function (that is, it has never existed before).

If a file is reopened after calling close(), the same file will be opened again.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.setFileTemplate`, QT_USE_NODISCARD_FILE_OPEN.
