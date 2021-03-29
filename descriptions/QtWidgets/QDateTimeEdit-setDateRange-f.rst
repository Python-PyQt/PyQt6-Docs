.. sip:method-description::
    :status: todo
    :pysig: 919838eba3424077f18321b86d76155e
    :realsig: (QDate,QDate)
    :digest: 2d78242e8d684f96b1d09937549e2552

Set the range of allowed dates for the date time edit.

This convenience function sets the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDate` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDate` properties.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 73-73

is analogous to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 78-79

If either *min* or *max* is invalid, this function does nothing. This function preserves the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumTime` property. If *max* is less than *min*, the new :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDateTime` property shall be the new :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDateTime` property. If *max* is equal to *min* and the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumTime` property was less then the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumTime` property, the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumTime` property is set to the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumTime` property. Otherwise, this preserves the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumTime` property.

If the range is narrower then a time interval whose end it spans, for example a week that spans the end of a month, users can only edit the date to one in the later part of the range if keyboard-tracking is disabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDate`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDate`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setDateTimeRange`, :sip:ref:`~PyQt6.QtCore.QDate.isValid`, :ref:`qdatetimeedit-keyboard-tracking`.
