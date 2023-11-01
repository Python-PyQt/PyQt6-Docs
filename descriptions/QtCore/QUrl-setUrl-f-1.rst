.. sip:method-description::
    :status: todo
    :pysig: 68e9f7176d2fd3d9da14bf66cc218b40
    :realsig: (const QString&, QUrl::ParsingMode)
    :digest: 4e871a8a994464b34bdfc361aaba9dfd

Parses *url* and sets this object to that value. :sip:ref:`~PyQt6.QtCore.QUrl` will automatically percent encode all characters that are not allowed in a URL and decode the percent-encoded sequences that represent an unreserved character (letters, digits, hyphens, underscores, dots and tildes). All other characters are left in their original forms.

Parses the *url* using the parser mode *parsingMode*. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode` (the default), :sip:ref:`~PyQt6.QtCore.QUrl` will correct certain mistakes, notably the presence of a percent character ('%') not followed by two hexadecimal digits, and it will accept any character in any position. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, encoding mistakes will not be tolerated and :sip:ref:`~PyQt6.QtCore.QUrl` will also check that certain forbidden characters are not present in unencoded form. If an error is detected in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, :sip:ref:`~PyQt6.QtCore.QUrl.isValid` will return false. The parsing mode :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is not permitted in this context and will produce a run-time warning.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.url`, :sip:ref:`~PyQt6.QtCore.QUrl.toString`.
