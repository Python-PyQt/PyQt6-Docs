.. sip:class-description::
    :status: todo
    :brief: Simple CBOR stream decoder, operating on either a QByteArray or QIODevice
    :digest: e4cabb849a737a1de2fca3a4fbf28231

The :sip:ref:`~PyQt6.QtCore.QCborStreamReader` class is a simple CBOR stream decoder, operating on either a :sip:ref:`~PyQt6.QtCore.QByteArray` or :sip:ref:`~PyQt6.QtCore.QIODevice`.

This class can be used to decode a stream of CBOR content directly from either a :sip:ref:`~PyQt6.QtCore.QByteArray` or a :sip:ref:`~PyQt6.QtCore.QIODevice`. CBOR is the Concise Binary Object Representation, a very compact form of binary data encoding that is compatible with JSON. It was created by the IETF Constrained RESTful Environments (CoRE) WG, which has used it in many new RFCs. It is meant to be used alongside the CoAP protocol.

:sip:ref:`~PyQt6.QtCore.QCborStreamReader` provides a StAX-like API, similar to that of :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`. Using it requires a bit of knowledge of CBOR encoding. For a simpler API, see QCborValue and especially the decoding function QCborValue::fromCbor().

Typically, one creates a :sip:ref:`~PyQt6.QtCore.QCborStreamReader` by passing the source :sip:ref:`~PyQt6.QtCore.QByteArray` or :sip:ref:`~PyQt6.QtCore.QIODevice` as a parameter to the constructor, then pop elements off the stream if there were no errors in decoding. There are three kinds of CBOR types:

+-------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Kind        | Types                                        | Behavior                                                                                                                                                                                                                                                              |
+=============+==============================================+=======================================================================================================================================================================================================================================================================+
| Fixed-width | Integers, Tags, Simple types, Floating point | Value is pre-parsed by :sip:ref:`~PyQt6.QtCore.QCborStreamReader`, so accessor functions are ``const``. Must call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.next` to advance.                                                                                         |
+-------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Strings     | Byte arrays, Text strings                    | Length (if known) is pre-parsed, but the string itself is not. The accessor functions are not const and may allocate memory. Once called, the accessor functions automatically advance to the next element.                                                           |
+-------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Containers  | Arrays, Maps                                 | Length (if known) is pre-parsed. To access the elements, you must call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer`, read all elements, then call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`. That function advances to the next element. |
+-------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

So a processor function typically looks like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 257-281

.. _qcborstreamreader-cbor-support:

CBOR support
------------

The following table lists the CBOR features that :sip:ref:`~PyQt6.QtCore.QCborStreamReader` supports.

+-----------------------------------------------+------------------+
| Feature                                       | Support          |
+===============================================+==================+
| Unsigned numbers                              | Yes (full range) |
+-----------------------------------------------+------------------+
| Negative numbers                              | Yes (full range) |
+-----------------------------------------------+------------------+
| Byte strings                                  | Yes              |
+-----------------------------------------------+------------------+
| Text strings                                  | Yes              |
+-----------------------------------------------+------------------+
| Chunked strings                               | Yes              |
+-----------------------------------------------+------------------+
| Tags                                          | Yes (arbitrary)  |
+-----------------------------------------------+------------------+
| Booleans                                      | Yes              |
+-----------------------------------------------+------------------+
| Null                                          | Yes              |
+-----------------------------------------------+------------------+
| Undefined                                     | Yes              |
+-----------------------------------------------+------------------+
| Arbitrary simple values                       | Yes              |
+-----------------------------------------------+------------------+
| Half-precision float (16-bit)                 | Yes              |
+-----------------------------------------------+------------------+
| Single-precision float (32-bit)               | Yes              |
+-----------------------------------------------+------------------+
| Double-precision float (64-bit)               | Yes              |
+-----------------------------------------------+------------------+
| Infinities and NaN floating point             | Yes              |
+-----------------------------------------------+------------------+
| Determinate-length arrays and maps            | Yes              |
+-----------------------------------------------+------------------+
| Indeterminate-length arrays and maps          | Yes              |
+-----------------------------------------------+------------------+
| Map key types other than strings and integers | Yes (arbitrary)  |
+-----------------------------------------------+------------------+

.. _qcborstreamreader-dealing-with-invalid-or-incomplete-cbor-streams:

Dealing with invalid or incomplete CBOR streams
-----------------------------------------------

:sip:ref:`~PyQt6.QtCore.QCborStreamReader` is capable of detecting corrupt input on its own. The library it uses has been extensively tested against invalid input of any kind and is quite able to report errors. If any is detected, :sip:ref:`~PyQt6.QtCore.QCborStreamReader` will set :sip:ref:`~PyQt6.QtCore.QCborStreamReader.lastError` to a value besides :sip:ref:`~PyQt6.QtCore.QCborError.Code.NoError`, indicating which situation was detected.

Most errors detected by :sip:ref:`~PyQt6.QtCore.QCborStreamReader` during normal item parsing are not recoverable. The code using :sip:ref:`~PyQt6.QtCore.QCborStreamReader` may opt to handle the data that was properly decoded or it can opt to discard the entire data.

The only recoverable error is :sip:ref:`~PyQt6.QtCore.QCborError.Code.EndOfFile`, which indicates that more data is required in order to complete the parsing. This situation is useful when data is being read from an asynchronous source, such as a pipe (\ :sip:ref:`~PyQt6.QtCore.QProcess`) or a socket (\ :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`, etc.). When more data arrives, the surrounding code needs to call either :sip:ref:`~PyQt6.QtCore.QCborStreamReader.addData`, if parsing from a :sip:ref:`~PyQt6.QtCore.QByteArray`, or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.reparse`, if it is instead reading directly a the QIDOevice that now has more data available (see :sip:ref:`~PyQt6.QtCore.QCborStreamReader.setDevice`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter`, QCborValue, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`, `Parsing and displaying CBOR data <https://doc.qt.io/qt-6/qtcore-serialization-cbordump-example.html>`_, `Serialization Converter <https://doc.qt.io/qt-6/qtcore-serialization-convert-example.html>`_, `Saving and Loading a Game <https://doc.qt.io/qt-6/qtcore-serialization-savegame-example.html>`_.
