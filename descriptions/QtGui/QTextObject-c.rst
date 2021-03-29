.. sip:class-description::
    :status: todo
    :brief: Base class for different kinds of objects that can group parts of a QTextDocument together
    :digest: 33a19a088defb37f63038e37e696164f

The :sip:ref:`~PyQt6.QtGui.QTextObject` class is a base class for different kinds of objects that can group parts of a :sip:ref:`~PyQt6.QtGui.QTextDocument` together.

The common grouping text objects are lists (\ :sip:ref:`~PyQt6.QtGui.QTextList`), frames (\ :sip:ref:`~PyQt6.QtGui.QTextFrame`), and tables (\ :sip:ref:`~PyQt6.QtGui.QTextTable`). A text object has an associated :sip:ref:`~PyQt6.QtGui.QTextObject.format` and :sip:ref:`~PyQt6.QtGui.QTextObject.document`.

There are essentially two kinds of text objects: those that are used with blocks (block formats), and those that are used with characters (character formats). The first kind are derived from :sip:ref:`~PyQt6.QtGui.QTextBlockGroup`, and the second kind from :sip:ref:`~PyQt6.QtGui.QTextFrame`.

You rarely need to use this class directly. When creating custom text objects, you will also need to reimplement :sip:ref:`~PyQt6.QtGui.QTextDocument.createObject` which acts as a factory method for creating text objects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument`, `Text Object Example <https://doc.qt.io/qt-6/qtsvg-richtext-textobject-example.html>`_.
