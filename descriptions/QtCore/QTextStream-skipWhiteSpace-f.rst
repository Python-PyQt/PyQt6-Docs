.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a2da37a47cc22697bcbd1a89f3d560eb

Reads and discards whitespace from the stream until either a non-space character is detected, or until :sip:ref:`~PyQt6.QtCore.QTextStream.atEnd` returns true. This function is useful when reading a stream character by character.

Whitespace characters are all characters for which QChar::isSpace() returns ``true``.

.. seealso:: operator>>().
