.. sip:class-description::
    :status: todo
    :brief: Format-independent interface for writing a QTextDocument to files or other devices
    :digest: dc317ff93df517236796c018a0cdb901

The :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` class provides a format-independent interface for writing a :sip:ref:`~PyQt6.QtGui.QTextDocument` to files or other devices.

To write a document, construct a :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` object with either a file name or a device object, and specify the document format to be written. You can construct a writer and set the format using :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.setFormat` later.

Call :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.write` to write the document to the device. If the document is successfully written, this function returns ``true``. However, if an error occurs when writing the document, it will return false.

Call :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter.supportedDocumentFormats` for a list of formats that :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter` can write.

Since the capabilities of the supported output formats vary considerably, the writer simply outputs the appropriate subset of objects for each format. This typically includes the formatted text and images contained in a document.
