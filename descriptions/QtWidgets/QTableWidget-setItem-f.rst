.. sip:method-description::
    :status: todo
    :pysig: b9a9f551429d00b04ffa75d1add0d3b9
    :realsig: (int,int,QTableWidgetItem*)
    :digest: 4b7c75633f31c77ad1fd0fa0f66dd709

Sets the item for the given *row* and *column* to *item*.

The table takes ownership of the item.

Note that if sorting is enabled (see sortingEnabled) and *column* is the current sort column, the *row* will be moved to the sorted position determined by *item*.

If you want to set several items of a particular row (say, by calling  in a loop), you may want to turn off sorting before doing so, and turn it back on afterwards; this will allow you to use the same *row* argument for all items in the same row (i.e.  will not move the row).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget.item`, :sip:ref:`~PyQt6.QtWidgets.QTableWidget.takeItem`.
