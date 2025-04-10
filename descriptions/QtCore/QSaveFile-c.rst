.. sip:class-description::
    :status: todo
    :brief: Interface for safely writing to files
    :digest: 1f62bb19400e4293959cb53822a36770

The :sip:ref:`~PyQt6.QtCore.QSaveFile` class provides an interface for safely writing to files.

:sip:ref:`~PyQt6.QtCore.QSaveFile` is an I/O device for writing text and binary files, without losing existing data if the writing operation fails.

While writing, the contents will be written to a temporary file, and if no error happened, :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` will move it to the final file. This ensures that no data at the final file is lost in case an error happens while writing, and no partially-written file is ever present at the final location. Always use :sip:ref:`~PyQt6.QtCore.QSaveFile` when saving entire documents to disk.

:sip:ref:`~PyQt6.QtCore.QSaveFile` automatically detects errors while writing, such as the full partition situation, where write() cannot write all the bytes. It will remember that an error happened, and will discard the temporary file in :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`.

Much like with :sip:ref:`~PyQt6.QtCore.QFile`, the file is opened with :sip:ref:`~PyQt6.QtCore.QSaveFile.open`. Data is usually read and written using :sip:ref:`~PyQt6.QtCore.QDataStream` or :sip:ref:`~PyQt6.QtCore.QTextStream`, but you can also directly call write().

Unlike :sip:ref:`~PyQt6.QtCore.QFile`, calling close() is not allowed. :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` replaces it. If :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` was not called and the :sip:ref:`~PyQt6.QtCore.QSaveFile` instance is destroyed, the temporary file is discarded.

To abort saving due to an application error, call :sip:ref:`~PyQt6.QtCore.QSaveFile.cancelWriting`, so that even a call to :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` later on will not save.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream`, :sip:ref:`~PyQt6.QtCore.QDataStream`, :sip:ref:`~PyQt6.QtCore.QFileInfo`, :sip:ref:`~PyQt6.QtCore.QDir`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile`.
