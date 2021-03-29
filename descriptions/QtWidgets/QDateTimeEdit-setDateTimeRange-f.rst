.. sip:method-description::
    :status: todo
    :pysig: 764245dfad54e076b13d5b932f8fb183
    :realsig: (const QDateTime&,const QDateTime&)
    :digest: 7c52f7b2adb31bc16c55660f50a98dc8

Set the range of allowed date-times for the date time edit.

This convenience function sets the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDateTime` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDateTime` properties.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 62-62

is analogous to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 67-68

If either *min* or *max* is invalid, this function does nothing. If *max* is less than *min*, *min* is used also as *max*.

If the range is narrower then a time interval whose end it spans, for example a week that spans the end of a month, users can only edit the date-time to one in the later part of the range if keyboard-tracking is disabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDateTime`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDateTime`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setDateRange`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setTimeRange`, :sip:ref:`~PyQt6.QtCore.QDateTime.isValid`, :ref:`qdatetimeedit-keyboard-tracking`.
