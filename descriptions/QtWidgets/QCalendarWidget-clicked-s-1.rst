.. sip:signal-description::
    :status: todo
    :pysig: 71520b00b20c9b4104450b3c40c360da
    :realsig: (QDate)
    :digest: d44e46d0077d1fbc1c7fce8d975b4210

This signal is emitted when a mouse button is clicked. The date the mouse was clicked on is specified by *date*. The signal is only emitted when clicked on a valid date, e.g., dates are not outside the :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.minimumDate` and :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.maximumDate`. If the selection mode is :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.SelectionMode.NoSelection`, this signal will not be emitted.
