.. sip:method-description::
    :status: todo
    :pysig: b5393c1269412f25f023441d6c5d74a9
    :realsig: (const QStringList&)
    :digest: b84b1761a1d0beb883a45107a2aa99d3

Parses the command line *arguments*.

Most programs don't need to call this, a simple call to :sip:ref:`~PyQt6.QtCore.QCommandLineParser.process` is enough.

is more low-level, and only does the parsing. The application will have to take care of the error handling, using :sip:ref:`~PyQt6.QtCore.QCommandLineParser.errorText` if  returns ``false``. This can be useful for instance to show a graphical error message in graphical programs.

Calling  instead of :sip:ref:`~PyQt6.QtCore.QCommandLineParser.process` can also be useful in order to ignore unknown options temporarily, because more option definitions will be provided later on (depending on one of the arguments), before calling :sip:ref:`~PyQt6.QtCore.QCommandLineParser.process`.

Don't forget that *arguments* must start with the name of the executable (ignored, though).

Returns ``false`` in case of a parse error (unknown option or missing value); returns ``true`` otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.process`.
