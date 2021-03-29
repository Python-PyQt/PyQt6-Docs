.. sip:class-description::
    :status: todo
    :brief: Encapsulates the different types of length used in a QTextDocument
    :digest: b398575480a8c39fe32cede036b3c151

The :sip:ref:`~PyQt6.QtGui.QTextLength` class encapsulates the different types of length used in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

When we specify a value for the length of an element in a text document, we often need to provide some other information so that the length is used in the way we expect. For example, when we specify a table width, the value can represent a fixed number of pixels, or it can be a percentage value. This information changes both the meaning of the value and the way it is used.

Generally, this class is used to specify table widths. These can be specified either as a fixed amount of pixels, as a percentage of the containing frame's width, or by a variable width that allows it to take up just the space it requires.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTable`.
