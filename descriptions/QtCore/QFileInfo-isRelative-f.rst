.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 70c7e3c1626b5542b2deeb4b01b50ba2

Returns ``true`` if the file system entry's path is relative, otherwise returns ``false`` (that is, the path is absolute).

On Unix, absolute paths begin with the directory separator ``'/'``. On Windows, absolute paths begin with a drive specification (for example, ``D:/``).

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isAbsolute`.
