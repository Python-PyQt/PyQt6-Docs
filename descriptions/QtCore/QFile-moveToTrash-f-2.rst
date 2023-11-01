.. sip:method-description::
    :status: todo
    :pysig: 50d17f6f521250cb9c7a582402c47b28
    :realsig: (const QString&, QString*)
    :digest: 6d3d5c7182a16c5d6afb6bb40f85a20c

This is an overloaded function.

Moves the file specified by :sip:ref:`~PyQt6.QtCore.QFile.fileName` to the trash. Returns ``true`` if successful, and sets *pathInTrash* (if provided) to the path at which the file can be found within the trash; otherwise returns ``false``.

**Note:** On systems where the system API doesn't report the path of the file in the trash, *pathInTrash* will be set to the null string once the file has been moved. On systems that don't have a trash can, this function always returns false.
