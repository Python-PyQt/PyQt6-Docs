.. sip:method-description::
    :status: todo
    :pysig: 68e9f7176d2fd3d9da14bf66cc218b40
    :realsig: (const QString&, QUrl::ParsingMode)
    :digest: 1e033153ccac2a67060be88b3704f9c2

Constructs a URL by parsing *url*. Note this constructor expects a proper URL or URL-Reference and will not attempt to guess intent. For example, the following declaration:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py

Will construct a valid URL but it may not be what one expects, as the :sip:ref:`~PyQt6.QtCore.QUrl.scheme` part of the input is missing. For a string like the above, applications may want to use :sip:ref:`~PyQt6.QtCore.QUrl.fromUserInput`. For this constructor or :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`, the following is probably what was intended:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py

:sip:ref:`~PyQt6.QtCore.QUrl` will automatically percent encode all characters that are not allowed in a URL and decode the percent-encoded sequences that represent an unreserved character (letters, digits, hyphens, underscores, dots and tildes). All other characters are left in their original forms.

Parses the *url* using the parser mode *parsingMode*. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode` (the default), :sip:ref:`~PyQt6.QtCore.QUrl` will correct certain mistakes, notably the presence of a percent character ('%') not followed by two hexadecimal digits, and it will accept any character in any position. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, encoding mistakes will not be tolerated and :sip:ref:`~PyQt6.QtCore.QUrl` will also check that certain forbidden characters are not present in unencoded form. If an error is detected in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, :sip:ref:`~PyQt6.QtCore.QUrl.isValid` will return false. The parsing mode :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is not permitted in this context.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 54-55

To construct a URL from an encoded string, you can also use :sip:ref:`~PyQt6.QtCore.QUrl.fromEncoded`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 60-60

Both functions are equivalent and, in Qt 5, both functions accept encoded data. Usually, the choice of the :sip:ref:`~PyQt6.QtCore.QUrl` constructor or :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` versus :sip:ref:`~PyQt6.QtCore.QUrl.fromEncoded` will depend on the source data: the constructor and :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` take a QString, whereas :sip:ref:`~PyQt6.QtCore.QUrl.fromEncoded` takes a :sip:ref:`~PyQt6.QtCore.QByteArray`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`, :sip:ref:`~PyQt6.QtCore.QUrl.fromEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`.
