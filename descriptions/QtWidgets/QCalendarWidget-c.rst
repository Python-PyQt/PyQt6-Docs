.. sip:class-description::
    :status: todo
    :brief: Monthly based calendar widget allowing the user to select a date
    :digest: c6c8f92683610a1f669e55d4e2d29044

The :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget` class provides a monthly based calendar widget allowing the user to select a date.

.. image:: ../../../images/fusion-calendarwidget.png

The widget is initialized with the current month and year, but :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget` provides several public slots to change the year and month that is shown.

By default, today's date is selected, and the user can select a date using both mouse and keyboard. The currently selected date can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.selectedDate` function. It is possible to constrain the user selection to a given date range by setting the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.minimumDate` and :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.maximumDate` properties. Alternatively, both properties can be set in one go using the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.setDateRange` convenience slot. Set the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.selectionMode` property to :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.SelectionMode.NoSelection` to prohibit the user from selecting at all. Note that a date also can be selected programmatically using the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.setSelectedDate` slot.

The currently displayed month and year can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.monthShown` and :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.yearShown` functions, respectively.

A newly created calendar widget uses abbreviated day names, and both Saturdays and Sundays are marked in red. The calendar grid is not visible. The week numbers are displayed, and the first column day is the first day of the week for the calendar's locale.

The notation of the days can be altered to a single letter abbreviations ("M" for "Monday") by setting the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.horizontalHeaderFormat` property to :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames`. Setting the same property to :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.LongDayNames` makes the header display the complete day names. The week numbers can be removed by setting the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.verticalHeaderFormat` property to :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader`. The calendar grid can be turned on by setting the gridVisible property to true using the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.setGridVisible` function:

+---------------------------------------------------------------------------------------------------------------+
| .. image:: ../../../images/qcalendarwidget-grid.png                                                           |
+---------------------------------------------------------------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qcalendarwidget.py |
|     :lines: 54-55                                                                                             |
+---------------------------------------------------------------------------------------------------------------+

Finally, the day in the first column can be altered using the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.setFirstDayOfWeek` function.

The :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget` class also provides three signals, :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.selectionChanged`, :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.activated` and :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.currentPageChanged` making it possible to respond to user interaction.

The rendering of the headers, weekdays or single days can be largely customized by setting :sip:ref:`~PyQt6.QtGui.QTextCharFormat`'s for some special weekday, a special date or for the rendering of the headers.

Only a subset of the properties in :sip:ref:`~PyQt6.QtGui.QTextCharFormat` are used by the calendar widget. Currently, the foreground, background and font properties are used to determine the rendering of individual cells in the widget.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtWidgets.QDateEdit`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat`.
