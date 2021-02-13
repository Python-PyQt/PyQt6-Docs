.. sip:signal-description::
    :status: todo
    :pysig: d666bcbd69a6565b11d1351e503738ee
    :realsig: (QGraphicsItem*,QGraphicsItem*,Qt::FocusReason)
    :digest: 018b7879db16ec52667d1771eb1d3af6

This signal is emitted by :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` whenever focus changes in the scene (i.e., when an item gains or loses input focus, or when focus passes from one item to another). You can connect to this signal if you need to keep track of when other items gain input focus. It is particularly useful for implementing virtual keyboards, input methods, and cursor items.

*oldFocusItem* is a pointer to the item that previously had focus, or 0 if no item had focus before the signal was emitted. *newFocusItem* is a pointer to the item that gained input focus, or ``nullptr`` if focus was lost. *reason* is the reason for the focus change (e.g., if the scene was deactivated while an input field had focus, *oldFocusItem* would point to the input field item, *newFocusItem* would be ``nullptr``, and *reason* would be :sip:ref:`~PyQt6.QtCore.Qt.FocusReason.ActiveWindowFocusReason`.
