.. sip:class-description::
    :status: todo
    :brief: Convenient interface for reading and writing text
    :digest: 4a0f941f4b896ef45d1fe41e964bdf1b

The :sip:ref:`~PyQt6.QtCore.QTextStream` class provides a convenient interface for reading and writing text.

:sip:ref:`~PyQt6.QtCore.QTextStream` can operate on a :sip:ref:`~PyQt6.QtCore.QIODevice`, a :sip:ref:`~PyQt6.QtCore.QByteArray` or a QString. Using :sip:ref:`~PyQt6.QtCore.QTextStream`'s streaming operators, you can conveniently read and write words, lines and numbers. For generating text, :sip:ref:`~PyQt6.QtCore.QTextStream` supports formatting options for field padding and alignment, and formatting of numbers. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtextstream.py
    :lines: 54-59

It's also common to use :sip:ref:`~PyQt6.QtCore.QTextStream` to read console input and write console output. :sip:ref:`~PyQt6.QtCore.QTextStream` is locale aware, and will automatically decode standard input using the correct encoding. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtextstream.py
    :lines: 64-68

Besides using :sip:ref:`~PyQt6.QtCore.QTextStream`'s constructors, you can also set the device or string :sip:ref:`~PyQt6.QtCore.QTextStream` operates on by calling :sip:ref:`~PyQt6.QtCore.QTextStream.setDevice` or setString(). You can seek to a position by calling :sip:ref:`~PyQt6.QtCore.QTextStream.seek`, and :sip:ref:`~PyQt6.QtCore.QTextStream.atEnd` will return true when there is no data left to be read. If you call :sip:ref:`~PyQt6.QtCore.QTextStream.flush`, :sip:ref:`~PyQt6.QtCore.QTextStream` will empty all data from its write buffer into the device and call :sip:ref:`~PyQt6.QtCore.QTextStream.flush` on the device.

Internally, :sip:ref:`~PyQt6.QtCore.QTextStream` uses a Unicode based buffer, and :sip:ref:`~PyQt6.QtCore.QStringConverter` is used by :sip:ref:`~PyQt6.QtCore.QTextStream` to automatically support different encodings. By default, UTF-8 is used for reading and writing, but you can also set the encoding by calling :sip:ref:`~PyQt6.QtCore.QTextStream.setEncoding`. Automatic Unicode detection is also supported. When this feature is enabled (the default behavior), :sip:ref:`~PyQt6.QtCore.QTextStream` will detect the UTF-8, UTF-16 or the UTF-32 BOM (Byte Order Mark) and switch to the appropriate UTF encoding when reading. :sip:ref:`~PyQt6.QtCore.QTextStream` does not write a BOM by default, but you can enable this by calling :sip:ref:`~PyQt6.QtCore.QTextStream.setGenerateByteOrderMark`\ (true). When :sip:ref:`~PyQt6.QtCore.QTextStream` operates on a QString directly, the encoding is disabled.

There are three general ways to use :sip:ref:`~PyQt6.QtCore.QTextStream` when reading text files:

* Chunk by chunk, by calling :sip:ref:`~PyQt6.QtCore.QTextStream.readLine` or :sip:ref:`~PyQt6.QtCore.QTextStream.readAll`.

* Word by word. :sip:ref:`~PyQt6.QtCore.QTextStream` supports streaming into QStrings, :sip:ref:`~PyQt6.QtCore.QByteArray`\ s and char\* buffers. Words are delimited by space, and leading white space is automatically skipped.

* Character by character, by streaming into QChar or char types. This method is often used for convenient input handling when parsing files, independent of character encoding and end-of-line semantics. To skip white space, call :sip:ref:`~PyQt6.QtCore.QTextStream.skipWhiteSpace`.

Since the text stream uses a buffer, you should not read from the stream using the implementation of a superclass. For instance, if you have a :sip:ref:`~PyQt6.QtCore.QFile` and read from it directly using QFile::readLine() instead of using the stream, the text stream's internal position will be out of sync with the file's position.

By default, when reading numbers from a stream of text, :sip:ref:`~PyQt6.QtCore.QTextStream` will automatically detect the number's base representation. For example, if the number starts with "0x", it is assumed to be in hexadecimal form. If it starts with the digits 1-9, it is assumed to be in decimal form, and so on. You can set the integer base, thereby disabling the automatic detection, by calling :sip:ref:`~PyQt6.QtCore.QTextStream.setIntegerBase`. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtextstream.py
    :lines: 73-80

:sip:ref:`~PyQt6.QtCore.QTextStream` supports many formatting options for generating text. You can set the field width and pad character by calling :sip:ref:`~PyQt6.QtCore.QTextStream.setFieldWidth` and :sip:ref:`~PyQt6.QtCore.QTextStream.setPadChar`. Use :sip:ref:`~PyQt6.QtCore.QTextStream.setFieldAlignment` to set the alignment within each field. For real numbers, call :sip:ref:`~PyQt6.QtCore.QTextStream.setRealNumberNotation` and :sip:ref:`~PyQt6.QtCore.QTextStream.setRealNumberPrecision` to set the notation (\ :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.SmartNotation`, :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.ScientificNotation`, :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.FixedNotation`) and precision in digits of the generated number. Some extra number formatting options are also available through :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`.

.. _qtextstream-qtextstream-manipulators:

Like ``<iostream>`` in the standard C++ library, :sip:ref:`~PyQt6.QtCore.QTextStream` also defines several global manipulator functions:

+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Manipulator                                 | Description                                                                                                                                                                              |
+=============================================+==========================================================================================================================================================================================+
| :sip:ref:`~PyQt6.QtCore.Qt.bin`             | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setIntegerBase`\ (2).                                                                                                                        |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.oct`             | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setIntegerBase`\ (8).                                                                                                                        |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.dec`             | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setIntegerBase`\ (10).                                                                                                                       |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.hex`             | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setIntegerBase`\ (16).                                                                                                                       |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.showbase`        | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` | :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.ShowBase`).           |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.forcesign`       | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` | :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.ForceSign`).          |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.forcepoint`      | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` | :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.ForcePoint`).         |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.noshowbase`      | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` & ~\ :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.ShowBase`).        |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.noforcesign`     | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` & ~\ :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.ForceSign`).       |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.noforcepoint`    | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` & ~\ :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.ForcePoint`).      |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.uppercasebase`   | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` | :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.UppercaseBase`).      |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.uppercasedigits` | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` | :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.UppercaseDigits`).    |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.lowercasebase`   | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` & ~\ :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.UppercaseBase`).   |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.lowercasedigits` | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setNumberFlags`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.numberFlags` & ~\ :sip:ref:`~PyQt6.QtCore.QTextStream.NumberFlags.UppercaseDigits`). |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.fixed`           | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setRealNumberNotation`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.FixedNotation`).                                           |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.scientific`      | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setRealNumberNotation`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.RealNumberNotation.ScientificNotation`).                                      |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.left`            | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setFieldAlignment`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.FieldAlignment.AlignLeft`).                                                       |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.right`           | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setFieldAlignment`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.FieldAlignment.AlignRight`).                                                      |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.center`          | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setFieldAlignment`\ (\ :sip:ref:`~PyQt6.QtCore.QTextStream.FieldAlignment.AlignCenter`).                                                     |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.endl`            | Same as operator<<('\\n') and :sip:ref:`~PyQt6.QtCore.QTextStream.flush`.                                                                                                                |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.flush`           | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.flush`.                                                                                                                                      |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.reset`           | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.reset`.                                                                                                                                      |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ws`              | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.skipWhiteSpace`.                                                                                                                             |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.bom`             | Same as :sip:ref:`~PyQt6.QtCore.QTextStream.setGenerateByteOrderMark`\ (true).                                                                                                           |
+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In addition, Qt provides three global manipulators that take a parameter: :sip:ref:`~PyQt6.QtCore.qSetFieldWidth`, :sip:ref:`~PyQt6.QtCore.qSetPadChar`, and :sip:ref:`~PyQt6.QtCore.qSetRealNumberPrecision`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream`, :sip:ref:`~PyQt6.QtCore.QIODevice`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QBuffer`.
