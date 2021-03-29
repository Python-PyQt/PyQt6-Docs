.. sip:class-description::
    :status: todo
    :brief: Allows you to define syntax highlighting rules, and in addition you can use the class to query a document's current formatting or user data
    :digest: fe2d8e4dbdc053cdae0827e8a06f0bd8

The :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter` class allows you to define syntax highlighting rules, and in addition you can use the class to query a document's current formatting or user data.

The :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter` class is a base class for implementing :sip:ref:`~PyQt6.QtGui.QTextDocument` syntax highlighters. A syntax highligher automatically highlights parts of the text in a :sip:ref:`~PyQt6.QtGui.QTextDocument`. Syntax highlighters are often used when the user is entering text in a specific format (for example source code) and help the user to read the text and identify syntax errors.

To provide your own syntax highlighting, you must subclass :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter` and reimplement :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.highlightBlock`.

When you create an instance of your :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter` subclass, pass it the :sip:ref:`~PyQt6.QtGui.QTextDocument` that you want the syntax highlighting to be applied to. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qsyntaxhighlighter.py
    :lines: 72-73

After this your :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.highlightBlock` function will be called automatically whenever necessary. Use your :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.highlightBlock` function to apply formatting (e.g. setting the font and color) to the text that is passed to it. :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter` provides the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.setFormat` function which applies a given :sip:ref:`~PyQt6.QtGui.QTextCharFormat` on the current text block. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qsyntaxhighlighter.py
    :lines: 78-90

.. _qsyntaxhighlighter-qsyntaxhighlighter-multiblock:

Some syntaxes can have constructs that span several text blocks. For example, a C++ syntax highlighter should be able to cope with ``/````\*...\*````/`` multiline comments. To deal with these cases it is necessary to know the end state of the previous text block (e.g. "in comment").

Inside your :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.highlightBlock` implementation you can query the end state of the previous text block using the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.previousBlockState` function. After parsing the block you can save the last state using :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.setCurrentBlockState`.

The :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.currentBlockState` and :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.previousBlockState` functions return an int value. If no state is set, the returned value is -1. You can designate any other value to identify any given state using the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.setCurrentBlockState` function. Once the state is set the :sip:ref:`~PyQt6.QtGui.QTextBlock` keeps that value until it is set set again or until the corresponding paragraph of text is deleted.

For example, if you're writing a simple C++ syntax highlighter, you might designate 1 to signify "in comment":

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qsyntaxhighlighter.py
    :lines: 95-121

In the example above, we first set the current block state to 0. Then, if the previous block ended within a comment, we highlight from the beginning of the current block (``startIndex = 0``). Otherwise, we search for the given start expression. If the specified end expression cannot be found in the text block, we change the current block state by calling :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.setCurrentBlockState`, and make sure that the rest of the block is highlighted.

In addition you can query the current formatting and user data using the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.format` and :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.currentBlockUserData` functions respectively. You can also attach user data to the current text block using the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.setCurrentBlockUserData` function. :sip:ref:`~PyQt6.QtGui.QTextBlockUserData` can be used to store custom settings. In the case of syntax highlighting, it is in particular interesting as cache storage for information that you may figure out while parsing the paragraph's text. For an example, see the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.setCurrentBlockUserData` documentation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument`, `Syntax Highlighter Example <https://doc.qt.io/qt-6/qtwidgets-richtext-syntaxhighlighter-example.html>`_.
