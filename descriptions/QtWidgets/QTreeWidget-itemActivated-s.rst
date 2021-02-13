.. sip:signal-description::
    :status: todo
    :pysig: b02c18642216501e93fcce63bc474bc3
    :realsig: (QTreeWidgetItem*,int)
    :digest: 1ffebeb5de519702d6e4361bf66a2f29

This signal is emitted when the user activates an item by single- or double-clicking (depending on the platform, i.e. on the :sip:ref:`~PyQt6.QtWidgets.QStyle.StyleHint.SH_ItemView_ActivateItemOnSingleClick` style hint) or pressing a special key (e.g., Enter).

The specified *item* is the item that was clicked, or ``nullptr`` if no item was clicked. The *column* is the item's column that was clicked, or -1 if no item was clicked.
