.. sip:method-description::
    :status: todo
    :pysig: af193f7da54d4df813f044d1a85c747b
    :realsig: (const QModelIndex&)
    :digest: bcb6489d16404bed8f75f1b941162331

Sets the current index to the row of the *index* if the orientation is horizontal (the default), otherwise to the column of the *index*.

Calls :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex` internally. This convenience slot can be connected to the signal :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentRowChanged` or :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.currentColumnChanged` of another view's :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`.

The following example illustrates how to update all widgets with new data whenever the selection of a :sip:ref:`~PyQt6.QtWidgets.QTableView` named ``myTableView`` changes:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qdatawidgetmapper.py
    :lines: 72-74

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.currentIndex`.
