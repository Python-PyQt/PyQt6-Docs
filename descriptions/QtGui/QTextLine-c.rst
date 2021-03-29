.. sip:class-description::
    :status: todo
    :brief: Represents a line of text inside a QTextLayout
    :digest: a480791ec0ab83961f3b58568e6aba19

The :sip:ref:`~PyQt6.QtGui.QTextLine` class represents a line of text inside a :sip:ref:`~PyQt6.QtGui.QTextLayout`.

A text line is usually created by :sip:ref:`~PyQt6.QtGui.QTextLayout.createLine`.

After being created, the line can be filled using the :sip:ref:`~PyQt6.QtGui.QTextLine.setLineWidth` or :sip:ref:`~PyQt6.QtGui.QTextLine.setNumColumns` functions. A line has a number of attributes including the rectangle it occupies, :sip:ref:`~PyQt6.QtGui.QTextLine.rect`, its coordinates, :sip:ref:`~PyQt6.QtGui.QTextLine.x` and :sip:ref:`~PyQt6.QtGui.QTextLine.y`, its :sip:ref:`~PyQt6.QtGui.QTextLine.textLength`, :sip:ref:`~PyQt6.QtGui.QTextLine.width` and :sip:ref:`~PyQt6.QtGui.QTextLine.naturalTextWidth`, and its :sip:ref:`~PyQt6.QtGui.QTextLine.ascent` and :sip:ref:`~PyQt6.QtGui.QTextLine.descent` relative to the text. The position of the cursor in terms of the line is available from :sip:ref:`~PyQt6.QtGui.QTextLine.cursorToX` and its inverse from :sip:ref:`~PyQt6.QtGui.QTextLine.xToCursor`. A line can be moved with :sip:ref:`~PyQt6.QtGui.QTextLine.setPosition`.
