.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 104c387b84111140b76130bd0f4eaeec

Moves the file specified by :sip:ref:`~PyQt6.QtCore.QFile.fileName` to the trash. Returns ``true`` if successful, and sets the :sip:ref:`~PyQt6.QtCore.QFile.fileName` to the path at which the file can be found within the trash; otherwise returns ``false``.

**Note:** On systems where the system API doesn't report the location of the file in the trash, :sip:ref:`~PyQt6.QtCore.QFile.fileName` will be set to the null string once the file has been moved. On systems that don't have a trash can, this function always returns false.
