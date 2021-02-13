.. sip:class-description::
    :status: todo
    :brief: Abstract base class used to implement custom layouts for QTextDocuments
    :digest: 7e3f4ddce3a42454eeffd28c506b0c5e

The :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` class is an abstract base class used to implement custom layouts for QTextDocuments.

The standard layout provided by Qt can handle simple word processing including inline images, lists and tables.

Some applications, e.g., a word processor or a DTP application might need more features than the ones provided by Qt's layout engine, in which case you can subclass :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` to provide custom layout behavior for your text documents.

An instance of the :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` subclass can be installed on a :sip:ref:`~PyQt6.QtGui.QTextDocument` object with the :sip:ref:`~PyQt6.QtGui.QTextDocument.setDocumentLayout` function.

You can insert custom objects into a :sip:ref:`~PyQt6.QtGui.QTextDocument`; see the :sip:ref:`~PyQt6.QtGui.QTextObjectInterface` class description for details.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextObjectInterface`.
