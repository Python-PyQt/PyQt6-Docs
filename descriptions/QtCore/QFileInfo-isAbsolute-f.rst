.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9a2b1049b138547298d9e785e5ac4f8d

Returns ``true`` if the file path is absolute, otherwise returns ``false`` (i.e. the path is relative).

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`.
