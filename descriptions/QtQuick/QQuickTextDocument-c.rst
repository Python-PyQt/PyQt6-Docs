.. sip:class-description::
    :status: todo
    :brief: Access to the QTextDocument of QQuickTextEdit
    :digest: 2497647d04624375b284c83c55173a4a

The :sip:ref:`~PyQt6.QtQuick.QQuickTextDocument` class provides access to the :sip:ref:`~PyQt6.QtGui.QTextDocument` of QQuickTextEdit.

This class provides access to the :sip:ref:`~PyQt6.QtGui.QTextDocument` of QQuickTextEdit elements. This is provided to allow usage of the `Rich Text Processing <https://doc.qt.io/qt-6/richtext.html>`_ functionalities of Qt. You are not allowed to modify the document, but it can be used to output content, for example with :sip:ref:`~PyQt6.QtGui.QTextDocumentWriter`), or provide additional formatting, for example with :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter`.

The class has to be used from C++ directly, using the property of the `TextEdit <https://doc.qt.io/qt-6/qml-qtquick-textedit.html>`_.

Warning: The :sip:ref:`~PyQt6.QtGui.QTextDocument` provided is used internally by `Qt Quick <https://doc.qt.io/qt-6/qtquick-index.html>`_ elements to provide text manipulation primitives. You are not allowed to perform any modification of the internal state of the :sip:ref:`~PyQt6.QtGui.QTextDocument`. If you do, the element in question may stop functioning or crash.
