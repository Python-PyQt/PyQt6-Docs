.. sip:class-description::
    :status: todo
    :brief: Used to lay out and render text
    :digest: d124e6c402fa4368593cb6fe5ec5ae2f

The :sip:ref:`~PyQt6.QtGui.QTextLayout` class is used to lay out and render text.

It offers many features expected from a modern text layout engine, including Unicode compliant rendering, line breaking and handling of cursor positioning. It can also produce and render device independent layout, something that is important for WYSIWYG applications.

The class has a rather low level API and unless you intend to implement your own text rendering for some specialized widget, you probably won't need to use it directly.

:sip:ref:`~PyQt6.QtGui.QTextLayout` can be used with both plain and rich text.

:sip:ref:`~PyQt6.QtGui.QTextLayout` can be used to create a sequence of :sip:ref:`~PyQt6.QtGui.QTextLine` instances with given widths and can position them independently on the screen. Once the layout is done, these lines can be drawn on a paint device.

The text to be laid out can be provided in the constructor or set with :sip:ref:`~PyQt6.QtGui.QTextLayout.setText`.

The layout can be seen as a sequence of :sip:ref:`~PyQt6.QtGui.QTextLine` objects; use :sip:ref:`~PyQt6.QtGui.QTextLayout.createLine` to create a :sip:ref:`~PyQt6.QtGui.QTextLine` instance, and :sip:ref:`~PyQt6.QtGui.QTextLayout.lineAt` or :sip:ref:`~PyQt6.QtGui.QTextLayout.lineForTextPosition` to retrieve created lines.

Here is a code snippet that demonstrates the layout phase:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qtextlayout.py
    :lines: 72-86

The text can then be rendered by calling the layout's :sip:ref:`~PyQt6.QtGui.QTextLayout.draw` function:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qtextlayout.py
    :lines: 95-96

For a given position in the text you can find a valid cursor position with :sip:ref:`~PyQt6.QtGui.QTextLayout.isValidCursorPosition`, :sip:ref:`~PyQt6.QtGui.QTextLayout.nextCursorPosition`, and :sip:ref:`~PyQt6.QtGui.QTextLayout.previousCursorPosition`.

The :sip:ref:`~PyQt6.QtGui.QTextLayout` itself can be positioned with :sip:ref:`~PyQt6.QtGui.QTextLayout.setPosition`; it has a :sip:ref:`~PyQt6.QtGui.QTextLayout.boundingRect`, and a :sip:ref:`~PyQt6.QtGui.QTextLayout.minimumWidth` and a :sip:ref:`~PyQt6.QtGui.QTextLayout.maximumWidth`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStaticText`.
