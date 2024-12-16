:orphan:

.. sip:class:: PyQt6.QtWidgets.QCalendarWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QCalendarWidget-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat
        :description: QtWidgets/QCalendarWidget-HorizontalHeaderFormat-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.LongDayNames
            :description: QtWidgets/QCalendarWidget-HorizontalHeaderFormat-LongDayNames-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader
            :description: QtWidgets/QCalendarWidget-HorizontalHeaderFormat-NoHorizontalHeader-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames
            :description: QtWidgets/QCalendarWidget-HorizontalHeaderFormat-ShortDayNames-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames
            :description: QtWidgets/QCalendarWidget-HorizontalHeaderFormat-SingleLetterDayNames-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QCalendarWidget.SelectionMode
        :description: QtWidgets/QCalendarWidget-SelectionMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.SelectionMode.NoSelection
            :description: QtWidgets/QCalendarWidget-SelectionMode-NoSelection-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.SelectionMode.SingleSelection
            :description: QtWidgets/QCalendarWidget-SelectionMode-SingleSelection-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QCalendarWidget.VerticalHeaderFormat
        :description: QtWidgets/QCalendarWidget-VerticalHeaderFormat-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.VerticalHeaderFormat.ISOWeekNumbers
            :description: QtWidgets/QCalendarWidget-VerticalHeaderFormat-ISOWeekNumbers-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
            :description: QtWidgets/QCalendarWidget-VerticalHeaderFormat-NoVerticalHeader-v.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QCalendarWidget-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.calendar
        :returns:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :description: QtWidgets/QCalendarWidget-calendar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.clearMaximumDate
        :description: QtWidgets/QCalendarWidget-clearMaximumDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.clearMinimumDate
        :description: QtWidgets/QCalendarWidget-clearMinimumDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.dateEditAcceptDelay
        :returns:
            int
        :description: QtWidgets/QCalendarWidget-dateEditAcceptDelay-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.dateTextFormat
        :returns:
            dict[:sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat`]
        :description: QtWidgets/QCalendarWidget-dateTextFormat-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.dateTextFormat
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QCalendarWidget-dateTextFormat-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QCalendarWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QCalendarWidget-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.firstDayOfWeek
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DayOfWeek`
        :description: QtWidgets/QCalendarWidget-firstDayOfWeek-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.headerTextFormat
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QCalendarWidget-headerTextFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.horizontalHeaderFormat
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat`
        :description: QtWidgets/QCalendarWidget-horizontalHeaderFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.isDateEditEnabled
        :returns:
            bool
        :description: QtWidgets/QCalendarWidget-isDateEditEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.isGridVisible
        :returns:
            bool
        :description: QtWidgets/QCalendarWidget-isGridVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.isNavigationBarVisible
        :returns:
            bool
        :description: QtWidgets/QCalendarWidget-isNavigationBarVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QCalendarWidget-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.maximumDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtWidgets/QCalendarWidget-maximumDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.minimumDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtWidgets/QCalendarWidget-minimumDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QCalendarWidget-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.monthShown
        :returns:
            int
        :description: QtWidgets/QCalendarWidget-monthShown-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QCalendarWidget-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.paintCell
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-paintCell-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QCalendarWidget-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.selectedDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDate`
        :description: QtWidgets/QCalendarWidget-selectedDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.selectionMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.SelectionMode`
        :description: QtWidgets/QCalendarWidget-selectionMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setCalendar
        :args:
            :sip:ref:`~PyQt6.QtCore.QCalendar`
        :description: QtWidgets/QCalendarWidget-setCalendar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setCurrentPage
        :args:
            int
            int
        :description: QtWidgets/QCalendarWidget-setCurrentPage-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setDateEditAcceptDelay
        :args:
            int
        :description: QtWidgets/QCalendarWidget-setDateEditAcceptDelay-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setDateEditEnabled
        :args:
            bool
        :description: QtWidgets/QCalendarWidget-setDateEditEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setDateRange
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-setDateRange-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setDateTextFormat
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QCalendarWidget-setDateTextFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setFirstDayOfWeek
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DayOfWeek`
        :description: QtWidgets/QCalendarWidget-setFirstDayOfWeek-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setGridVisible
        :args:
            bool
        :description: QtWidgets/QCalendarWidget-setGridVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setHeaderTextFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QCalendarWidget-setHeaderTextFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setHorizontalHeaderFormat
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.HorizontalHeaderFormat`
        :description: QtWidgets/QCalendarWidget-setHorizontalHeaderFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setMaximumDate
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-setMaximumDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setMinimumDate
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-setMinimumDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setNavigationBarVisible
        :args:
            bool
        :description: QtWidgets/QCalendarWidget-setNavigationBarVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setSelectedDate
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-setSelectedDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setSelectionMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.SelectionMode`
        :description: QtWidgets/QCalendarWidget-setSelectionMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setVerticalHeaderFormat
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.VerticalHeaderFormat`
        :description: QtWidgets/QCalendarWidget-setVerticalHeaderFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.setWeekdayTextFormat
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DayOfWeek`
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QCalendarWidget-setWeekdayTextFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.showNextMonth
        :description: QtWidgets/QCalendarWidget-showNextMonth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.showNextYear
        :description: QtWidgets/QCalendarWidget-showNextYear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.showPreviousMonth
        :description: QtWidgets/QCalendarWidget-showPreviousMonth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.showPreviousYear
        :description: QtWidgets/QCalendarWidget-showPreviousYear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.showSelectedDate
        :description: QtWidgets/QCalendarWidget-showSelectedDate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.showToday
        :description: QtWidgets/QCalendarWidget-showToday-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QCalendarWidget-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.updateCell
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-updateCell-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.updateCells
        :description: QtWidgets/QCalendarWidget-updateCells-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.verticalHeaderFormat
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCalendarWidget.VerticalHeaderFormat`
        :description: QtWidgets/QCalendarWidget-verticalHeaderFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.weekdayTextFormat
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DayOfWeek`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QCalendarWidget-weekdayTextFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QCalendarWidget.yearShown
        :returns:
            int
        :description: QtWidgets/QCalendarWidget-yearShown-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QCalendarWidget.activated
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-activated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QCalendarWidget.clicked
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDate`, datetime.date]
        :description: QtWidgets/QCalendarWidget-clicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QCalendarWidget.currentPageChanged
        :args:
            int
            int
        :description: QtWidgets/QCalendarWidget-currentPageChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QCalendarWidget.selectionChanged
        :description: QtWidgets/QCalendarWidget-selectionChanged-s.rst
