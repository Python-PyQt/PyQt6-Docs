.. sip:method-description::
    :status: todo
    :pysig: 06b6748bc0d5f7fc977b4321a5de7d3a
    :realsig: (QObject*, QEvent*)
    :digest: c60b4ea35d793ddfb9144f5da565ce61

Implements standard handling of events on behalf of the currently active *editor*. Call this function from an override of eventFilter() in a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` subclass, and return its result. To avoid duplicate event processing, do not call the parent class implementation of eventFilter() after calling this function.

Returns ``true`` if the given *editor* is a valid :sip:ref:`~PyQt6.QtWidgets.QWidget` and the given *event* is handled; otherwise returns ``false``. The following key press events are handled by default:

* Tab

* Backtab

* Enter

* Return

* Esc

If the *editor*'s type is :sip:ref:`~PyQt6.QtWidgets.QTextEdit` or :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit` then Tab, Backtab, Enter and Return keys are *not* handled.

In the case of Tab, Backtab, Enter and Return key press events, the *editor*'s data is committed to the model and the editor is closed. If the *event* is a Tab key press the view will open an editor on the next item in the view. Likewise, if the *event* is a Backtab key press the view will open an editor on the *previous* item in the view.

If the event is a Esc key press event, the *editor* is closed *without* committing its data.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.commitData`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor`.
