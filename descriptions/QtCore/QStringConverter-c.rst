.. sip:class-description::
    :status: todo
    :brief: Base class for encoding and decoding text
    :digest: 8df35b02c79f1247af4a6bf4f80f4f36

The :sip:ref:`~PyQt6.QtCore.QStringConverter` class provides a base class for encoding and decoding text.

Qt uses UTF-16 to store, draw and manipulate strings. In many situations you may wish to deal with data that uses a different encoding. Most text data transferred over files and network connections is encoded in UTF-8.

The :sip:ref:`~PyQt6.QtCore.QStringConverter` class is a base class for the :sip:ref:`~PyQt6.QtCore.QStringEncoder` and :sip:ref:`~PyQt6.QtCore.QStringDecoder` classes that help with converting between different text encodings. :sip:ref:`~PyQt6.QtCore.QStringDecoder` can decode a string from an encoded representation into UTF-16, the format Qt uses internally. :sip:ref:`~PyQt6.QtCore.QStringEncoder` does the opposite operation, encoding UTF-16 encoded data (usually in the form of a QString) to the requested encoding.

The supported encodings are:

* UTF-8

* UTF-16

* UTF-16BE

* UTF-16LE

* UTF-32

* UTF-32BE

* UTF-32LE

* ISO-8859-1 (Latin-1)

* The system encoding

:sip:ref:`~PyQt6.QtCore.QStringConverter`\ s can be used as follows to convert some encoded string to and from UTF-16.

Suppose you have some string encoded in UTF-8, and want to convert it to a QString. The simple way to do it is to use a :sip:ref:`~PyQt6.QtCore.QStringDecoder` like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 54-56

After this, ``string`` holds the text in decoded form. Converting a string from Unicode to the local encoding is just as easy using the :sip:ref:`~PyQt6.QtCore.QStringEncoder` class:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 61-63

To read or write text files in various encodings, use :sip:ref:`~PyQt6.QtCore.QTextStream` and its :sip:ref:`~PyQt6.QtCore.QTextStream.setEncoding` function.

Some care must be taken when trying to convert the data in chunks, for example, when receiving it over a network. In such cases it is possible that a multi-byte character will be split over two chunks. At best this might result in the loss of a character and at worst cause the entire conversion to fail.

Both :sip:ref:`~PyQt6.QtCore.QStringEncoder` and :sip:ref:`~PyQt6.QtCore.QStringDecoder` make this easy, by tracking this in an internal state. So simply calling the encoder or decoder again with the next chunk of data will automatically continue encoding or decoding the data correctly:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qstringconverter.py
    :lines: 68-74

The :sip:ref:`~PyQt6.QtCore.QStringDecoder` object maintains state between chunks and therefore works correctly even if a multi-byte character is split between chunks.

:sip:ref:`~PyQt6.QtCore.QStringConverter` objects can't be copied because of their internal state, but can be moved.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream`, :sip:ref:`~PyQt6.QtCore.QStringDecoder`, :sip:ref:`~PyQt6.QtCore.QStringEncoder`.
