.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 413116d3f2cbe538cfc6d928a352b9c8

Returns ``true`` if the file path is relative, otherwise returns ``false`` (i.e. the path is absolute). (E.g. under Unix a path is absolute if it begins with a "/").

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isAbsolute`.
