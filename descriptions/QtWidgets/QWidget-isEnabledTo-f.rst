.. sip:method-description::
    :status: todo
    :pysig: c0199cb465a8cea34ddeb3b3f26b2747
    :realsig: (const QWidget*) const
    :digest: 72f93ea0a8386fc7e326a8b39d2b3c92

Returns ``true`` if this widget would become enabled if *ancestor* is enabled; otherwise returns ``false``.

This is the case if neither the widget itself nor every parent up to but excluding *ancestor* has been explicitly disabled.

isEnabledTo(0) returns false if this widget or any if its ancestors was explicitly disabled.

The word ancestor here means a parent widget within the same window.

Therefore isEnabledTo(0) stops at this widget's window, unlike :sip:ref:`~PyQt6.QtWidgets.QWidget.isEnabled` which also takes parent windows into considerations.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setEnabled`, enabled.
