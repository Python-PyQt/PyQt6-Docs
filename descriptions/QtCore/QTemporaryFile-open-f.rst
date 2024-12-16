.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: ceb66d6a526b5ab8c8d63998b10eeba9

A :sip:ref:`~PyQt6.QtCore.QTemporaryFile` will always be opened in QIODevice::ReadWrite mode, this allows easy access to the data in the file. This function will return true upon success and will set the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName` to the unique filename used.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName`, QT_USE_NODISCARD_FILE_OPEN.
