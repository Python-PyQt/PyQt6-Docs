.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 0582fa16a9eaa59f5c887c71a925e01d

Returns an error message if the last operation that modified this :sip:ref:`~PyQt6.QtCore.QUrl` object ran into a parsing error. If no error was detected, this function returns an empty string and :sip:ref:`~PyQt6.QtCore.QUrl.isValid` returns ``true``.

The error message returned by this function is technical in nature and may not be understood by end users. It is mostly useful to developers trying to understand why :sip:ref:`~PyQt6.QtCore.QUrl` will not accept some input.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode`.
