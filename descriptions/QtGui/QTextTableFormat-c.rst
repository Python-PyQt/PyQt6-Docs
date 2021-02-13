.. sip:class-description::
    :status: todo
    :brief: Formatting information for tables in a QTextDocument
    :digest: 1b79d9dad3d4699962913810040bbd03

The :sip:ref:`~PyQt6.QtGui.QTextTableFormat` class provides formatting information for tables in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A table is a group of cells ordered into rows and columns. Each table contains at least one row and one column. Each cell contains a block. Tables in rich text documents are formatted using the properties defined in this class.

Tables are horizontally justified within their parent frame according to the table's alignment. This can be read with the :sip:ref:`~PyQt6.QtGui.QTextTableFormat.alignment` function and set with :sip:ref:`~PyQt6.QtGui.QTextTableFormat.setAlignment`.

Cells within the table are separated by cell spacing. The number of pixels between cells is set with :sip:ref:`~PyQt6.QtGui.QTextTableFormat.setCellSpacing` and read with :sip:ref:`~PyQt6.QtGui.QTextTableFormat.cellSpacing`. The contents of each cell is surrounded by cell padding. The number of pixels between each cell edge and its contents is set with :sip:ref:`~PyQt6.QtGui.QTextTableFormat.setCellPadding` and read with :sip:ref:`~PyQt6.QtGui.QTextTableFormat.cellPadding`.

.. image:: ../../../images/qtexttableformat-cell.png

The table's background color can be read with the background() function, and can be specified with setBackground(). The background color of each cell can be set independently, and will control the color of the cell within the padded area.

The table format also provides a way to constrain the widths of the columns in the table. Columns can be assigned a fixed width, a variable width, or a percentage of the available width (see :sip:ref:`~PyQt6.QtGui.QTextLength`). The :sip:ref:`~PyQt6.QtGui.QTextTableFormat.columns` function returns the number of columns with constraints, and the :sip:ref:`~PyQt6.QtGui.QTextTableFormat.columnWidthConstraints` function returns the constraints defined for the table. These quantities can also be set by calling :sip:ref:`~PyQt6.QtGui.QTextTableFormat.setColumnWidthConstraints` with a list containing new constraints. If no constraints are required, :sip:ref:`~PyQt6.QtGui.QTextTableFormat.clearColumnWidthConstraints` can be used to remove them.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTable`, :sip:ref:`~PyQt6.QtGui.QTextTableCell`, :sip:ref:`~PyQt6.QtGui.QTextLength`.
