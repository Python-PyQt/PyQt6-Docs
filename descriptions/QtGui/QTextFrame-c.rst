.. sip:class-description::
    :status: todo
    :brief: Represents a frame in a QTextDocument
    :digest: 7642ba9443e3b5f2ca76bdb7345a2996

The :sip:ref:`~PyQt6.QtGui.QTextFrame` class represents a frame in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

Text frames provide structure for the text in a document. They are used as generic containers for other document elements. Frames are usually created by using :sip:ref:`~PyQt6.QtGui.QTextCursor.insertFrame`.

Frames can be used to create hierarchical structures in rich text documents. Each document has a root frame (\ :sip:ref:`~PyQt6.QtGui.QTextDocument.rootFrame`), and each frame beneath the root frame has a parent frame and a (possibly empty) list of child frames. The parent frame can be found with :sip:ref:`~PyQt6.QtGui.QTextFrame.parentFrame`, and the :sip:ref:`~PyQt6.QtGui.QTextFrame.childFrames` function provides a list of child frames.

Each frame contains at least one text block to enable text cursors to insert new document elements within. As a result, the :sip:ref:`~PyQt6.QtGui.QTextFrame.iterator` class is used to traverse both the blocks and child frames within a given frame. The first and last child elements in the frame can be found with :sip:ref:`~PyQt6.QtGui.QTextFrame.begin` and :sip:ref:`~PyQt6.QtGui.QTextFrame.end`.

A frame also has a format (specified using :sip:ref:`~PyQt6.QtGui.QTextFrameFormat`) which can be set with setFormat() and read with format().

Text cursors can be obtained that point to the first and last valid cursor positions within a frame; use the :sip:ref:`~PyQt6.QtGui.QTextFrame.firstCursorPosition` and :sip:ref:`~PyQt6.QtGui.QTextFrame.lastCursorPosition` functions for this. The frame's extent in the document can be found with :sip:ref:`~PyQt6.QtGui.QTextFrame.firstPosition` and :sip:ref:`~PyQt6.QtGui.QTextFrame.lastPosition`.

You can iterate over a frame's contents using the :sip:ref:`~PyQt6.QtGui.QTextFrame.iterator` class: this provides read-only access to its internal list of text blocks and child frames.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor`, :sip:ref:`~PyQt6.QtGui.QTextDocument`.
