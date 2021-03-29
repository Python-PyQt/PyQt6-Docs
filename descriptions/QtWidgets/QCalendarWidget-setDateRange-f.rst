.. sip:method-description::
    :status: todo
    :pysig: 919838eba3424077f18321b86d76155e
    :realsig: (QDate,QDate)
    :digest: 60e9dd699e228651253242f1fd918b13

Defines a date range by setting the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.minimumDate` and :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.maximumDate` properties.

The date range restricts the user selection, i.e. the user can only select dates within the specified date range. Note that

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qcalendarwidget.py
    :lines: 74-76

is analogous to

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qcalendarwidget.py
    :lines: 81-84

If either the *min* or *max* parameters are not valid :sip:ref:`~PyQt6.QtCore.QDate` objects, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.setMinimumDate`, :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.setMaximumDate`.
