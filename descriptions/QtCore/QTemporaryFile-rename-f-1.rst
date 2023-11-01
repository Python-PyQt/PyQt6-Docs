.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 12fb7551ab634c3630404904e2e7249f

Renames the current temporary file to *newName* and returns true if it succeeded.

This function has an important difference compared to :sip:ref:`~PyQt6.QtCore.QFile.rename`: it will not perform a copy+delete if the low-level system call to rename the file fails, something that could happen if *newName* specifies a file in a different volume or filesystem than the temporary file was created on. In other words, :sip:ref:`~PyQt6.QtCore.QTemporaryFile` only supports atomic file renaming.

This functionality is intended to support materializing the destination file with all contents already present, so another process cannot see an incomplete file in the process of being written. The :sip:ref:`~PyQt6.QtCore.QSaveFile` class can be used for a similar purpose too, particularly if the destination file is not temporary.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSaveFile`, :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`, :sip:ref:`~PyQt6.QtCore.QFile.rename`.
