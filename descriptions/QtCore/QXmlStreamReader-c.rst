.. sip:class-description::
    :status: todo
    :brief: Fast parser for reading well-formed XML via a simple streaming API
    :digest: 1dfd4c813cd14cb665dd06678520cf5e

The :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` class provides a fast parser for reading well-formed XML via a simple streaming API.

:sip:ref:`~PyQt6.QtCore.QXmlStreamReader` provides a simple streaming API to parse well-formed XML. It is an alternative to first loading the complete XML into a DOM tree (see :sip:ref:`~PyQt6.QtXml.QDomDocument`). :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` reads data either from a :sip:ref:`~PyQt6.QtCore.QIODevice` (see :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.setDevice`), or from a raw :sip:ref:`~PyQt6.QtCore.QByteArray` (see :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.addData`).

Qt provides :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` for writing XML.

The basic concept of a stream reader is to report an XML document as a stream of tokens, similar to SAX. The main difference between :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` and SAX is *how* these XML tokens are reported. With SAX, the application must provide handlers (callback functions) that receive so-called XML *events* from the parser at the parser's convenience. With :sip:ref:`~PyQt6.QtCore.QXmlStreamReader`, the application code itself drives the loop and pulls *tokens* from the reader, one after another, as it needs them. This is done by calling :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.readNext`, where the reader reads from the input stream until it completes the next token, at which point it returns the :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.tokenType`. A set of convenient functions including :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.isStartElement` and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.text` can then be used to examine the token to obtain information about what has been read. The big advantage of this *pulling* approach is the possibility to build recursive descent parsers with it, meaning you can split your XML parsing code easily into different methods or classes. This makes it easy to keep track of the application's own state when parsing XML.

A typical loop with :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` looks like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_xml_qxmlstream.py
    :lines: 54-62

:sip:ref:`~PyQt6.QtCore.QXmlStreamReader` is a well-formed XML 1.0 parser that does *not* include external parsed entities. As long as no error occurs, the application code can thus be assured that the data provided by the stream reader satisfies the W3C's criteria for well-formed XML. For example, you can be certain that all tags are indeed nested and closed properly, that references to internal entities have been replaced with the correct replacement text, and that attributes have been normalized or added according to the internal subset of the DTD.

If an error occurs while parsing, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.atEnd` and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.hasError` return true, and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.error` returns the error that occurred. The functions :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.errorString`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.lineNumber`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.columnNumber`, and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.characterOffset` are for constructing an appropriate error or warning message. To simplify application code, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` contains a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.raiseError` mechanism that lets you raise custom errors that trigger the same error handling described.

The `QXmlStream Bookmarks Example <https://doc.qt.io/qt-6/qtxml-streambookmarks-example.html>`_ illustrates how to use the recursive descent technique to read an XML bookmark file (XBEL) with a stream reader.

.. _qxmlstreamreader-namespaces:

Namespaces
----------

QXmlStream understands and resolves XML namespaces. E.g. in case of a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.StartElement`, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceUri` returns the namespace the element is in, and :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.name` returns the element's *local* name. The combination of :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceUri` and name uniquely identifies an element. If a namespace prefix was not declared in the XML entities parsed by the reader, the :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceUri` is empty.

If you parse XML data that does not utilize namespaces according to the XML specification or doesn't use namespaces at all, you can use the element's :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.qualifiedName` instead. A qualified name is the element's :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.prefix` followed by colon followed by the element's local :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.name` - exactly like the element appears in the raw XML data. Since the mapping :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceUri` to prefix is neither unique nor universal, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.qualifiedName` should be avoided for namespace-compliant XML data.

In order to parse standalone documents that do use undeclared namespace prefixes, you can turn off namespace processing completely with the :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.namespaceProcessing` property.

.. _qxmlstreamreader-incremental-parsing:

Incremental Parsing
-------------------

:sip:ref:`~PyQt6.QtCore.QXmlStreamReader` is an incremental parser. It can handle the case where the document can't be parsed all at once because it arrives in chunks (e.g. from multiple files, or over a network connection). When the reader runs out of data before the complete document has been parsed, it reports a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError`. When more data arrives, either because of a call to :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.addData` or because more data is available through the network :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.device`, the reader recovers from the :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError` error and continues parsing the new data with the next call to :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.readNext`.

For example, if your application reads data from the network using a network access manager, you would issue a network request to the manager and receive a network reply in return. Since a QNetworkReply is a :sip:ref:`~PyQt6.QtCore.QIODevice`, you connect its :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` signal to a custom slot, e.g. ``slotReadyRead()`` in the code snippet shown in the discussion for QNetworkAccessManager. In this slot, you read all available data with :sip:ref:`~PyQt6.QtCore.QIODevice.readAll` and pass it to the XML stream reader using :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.addData`. Then you call your custom parsing function that reads the XML events from the reader.

.. _qxmlstreamreader-performance-and-memory-consumption:

Performance and Memory Consumption
----------------------------------

:sip:ref:`~PyQt6.QtCore.QXmlStreamReader` is memory-conservative by design, since it doesn't store the entire XML document tree in memory, but only the current token at the time it is reported. In addition, :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` avoids the many small string allocations that it normally takes to map an XML document to a convenient and Qt-ish API. It does this by reporting all string data as `QStringView <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qstringview>`_ rather than real QString objects. Calling toString() on any of those objects returns an equivalent real QString object.
