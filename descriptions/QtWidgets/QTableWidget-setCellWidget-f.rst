.. sip:method-description::
    :status: todo
    :pysig: 9ed01bbe90558968a8579976aa1962f4
    :realsig: (int,int,QWidget*)
    :digest: 4280ef7edde9823132277548fd55b3e6

Sets the given *widget* to be displayed in the cell in the given *row* and *column*, passing the ownership of the widget to the table.

If cell widget A is replaced with cell widget B, cell widget A will be deleted. For example, in the code snippet below, the :sip:ref:`~PyQt6.QtWidgets.QLineEdit` object will be deleted.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qtablewidget.py
    :lines: 54-56

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget.cellWidget`.
