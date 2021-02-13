.. sip:signal-description::
    :status: todo
    :pysig: b02c18642216501e93fcce63bc474bc3
    :realsig: (QTreeWidgetItem*,int)
    :digest: 6e5642b9e3ca826fc91253386ad0a99e

This signal is emitted when the user double clicks inside the widget.

The specified *item* is the item that was clicked, or ``nullptr`` if no item was clicked. The *column* is the item's column that was clicked. If no item was double clicked, no signal will be emitted.
