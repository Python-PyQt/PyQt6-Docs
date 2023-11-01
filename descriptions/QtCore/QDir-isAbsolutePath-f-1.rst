.. sip:method-description::
    :status: todo
    :pysig: dd431a34e6382be8567cf5b44f2db6a6
    :realsig: (const QString&)
    :digest: 356db6dac3368c7ac83ff93b04d3e580

Returns ``true`` if *path* is absolute; returns ``false`` if it is relative.

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.isAbsolute`, :sip:ref:`~PyQt6.QtCore.QDir.isRelativePath`, :sip:ref:`~PyQt6.QtCore.QDir.makeAbsolute`, :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`, :sip:ref:`~PyQt6.QtCore.QResource`.
