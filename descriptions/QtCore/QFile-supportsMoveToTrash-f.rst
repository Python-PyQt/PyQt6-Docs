.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: ()
    :digest: d47f1ccf6bc7a7a6f0a2b3f244dea656

Returns ``true`` if Qt supports moving files to a trash (recycle bin) in the current operating system using the :sip:ref:`~PyQt6.QtCore.QFile.moveToTrash` function, ``false`` otherwise. Note that this function returning ``true`` does not imply :sip:ref:`~PyQt6.QtCore.QFile.moveToTrash` will succeed. In particular, this function does not check if the user has disabled the functionality in their settings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.moveToTrash`.
