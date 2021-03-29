.. sip:class-description::
    :status: todo
    :brief: Widget for editing dates and times
    :digest: 853fcf8ad7b2c87f8b567f1446913b41

The :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit` class provides a widget for editing dates and times.

.. image:: ../../../images/windows-datetimeedit.png

:sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit` allows the user to edit dates by using the keyboard or the arrow keys to increase and decrease date and time values. The arrow keys can be used to move from section to section within the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit` box. Dates and times appear in accordance with the format set; see :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setDisplayFormat`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 54-57

Here we've created a new :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit` object initialized with today's date, and restricted the valid date range to today plus or minus 365 days. We've set the order to month, day, year.

The range of valid values for a :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit` is controlled by the properties :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDateTime`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDateTime`, and their respective date and time components. By default, any date-time from the start of 100 CE to the end of 9999 CE is valid.

.. _qdatetimeedit-using-a-pop-up-calendar-widget:

Using a Pop-up Calendar Widget
------------------------------

:sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit` can be configured to allow a :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget` to be used to select dates. This is enabled by setting the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.calendarPopup` property. Additionally, you can supply a custom calendar widget for use as the calendar pop-up by calling the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setCalendarWidget` function. The existing calendar widget can be retrieved with :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.calendarWidget`.

.. _qdatetimeedit-keyboard-tracking:

Keyboard Tracking
-----------------

When :sip:ref:`~PyQt6.QtWidgets.QAbstractSpinBox.keyboardTracking` is enabled (the default), every keystroke of editing a field triggers signals for value changes.

When the allowed :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setDateTimeRange` is narrower than some time interval whose end it straddles, keyboard tracking prevents the user editing the date or time to access the later part of the interval. For example, for a range from 29.04.2020 to 02.05.2020 and an initial date of 30.04.2020, the user can change neither the month (May 30th is outside the range) nor the day (April 2nd is outside the range).

When keyboard tracking is disabled, changes are only signalled when focus leaves the text field after edits have modified the content. This allows the user to edit via an invalid date-time to reach a valid one.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDateEdit`, :sip:ref:`~PyQt6.QtWidgets.QTimeEdit`, :sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtCore.QTime`.
