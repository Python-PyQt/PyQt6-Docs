.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: bb1808764df5aae965de663a66810be9

By default, :sip:ref:`~PyQt6.QtGui.QTextTableFormat.borderCollapse` is ``true``, which has the following implications:

* The borders and grid of the table will be rendered following the CSS table ``border-collapse``: ``collapse`` rules

* Setting the ``border`` property to a minimum value of ``1`` will render a one pixel solid inner table grid using the borderBrush property and an outer border as specified

* The various border style properties of :sip:ref:`~PyQt6.QtGui.QTextTableCellFormat` can be used to customize the grid and have precedence over the border and grid of the table

* The :sip:ref:`~PyQt6.QtGui.QTextTableFormat.cellSpacing` property will be ignored

* For print pagination:

  * Columns continued on a page will not have their top cell border rendered

  * Repeated header rows will always have their bottom cell border rendered

With *borderCollapse* set to ``false``, cell borders can still be styled using :sip:ref:`~PyQt6.QtGui.QTextTableCellFormat` but styling will be applied only within the cell's frame, which is probably not very useful in practice.

**Note:** In Qt versions prior to 6.8, the default value was ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTableFormat.borderCollapse`, setBorder(), setBorderBrush(), setBorderStyle(), :sip:ref:`~PyQt6.QtGui.QTextTableCellFormat`.
