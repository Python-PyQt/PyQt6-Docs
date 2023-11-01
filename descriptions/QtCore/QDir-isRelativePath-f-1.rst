.. sip:method-description::
    :status: todo
    :pysig: dd431a34e6382be8567cf5b44f2db6a6
    :realsig: (const QString&)
    :digest: 7196fc4736f01c838aedad6597b2fd29

Returns ``true`` if *path* is relative; returns ``false`` if it is absolute.

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.isRelative`, :sip:ref:`~PyQt6.QtCore.QDir.isAbsolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.makeAbsolute`.
