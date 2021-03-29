.. sip:class-description::
    :status: todo
    :brief: Describes calendar systems
    :digest: 146acb224fd4678ef3d56909c3648355

The :sip:ref:`~PyQt6.QtCore.QCalendar` class describes calendar systems.

A :sip:ref:`~PyQt6.QtCore.QCalendar` object maps a year, month, and day-number to a specific day (ultimately identified by its Julian day number), using the rules of a particular system.

The default :sip:ref:`~PyQt6.QtCore.QCalendar` is a proleptic Gregorian calendar, which has no year zero. Other calendars may be supported by enabling suitable features or loading plugins. Calendars supported as features can be constructed by passing the :sip:ref:`~PyQt6.QtCore.QCalendar.System` enumeration to the constructor. All supported calendars may be constructed by name, once they have been constructed. (Thus plugins instantiate their calendar backend to register it.) Built-in backends, accessible via :sip:ref:`~PyQt6.QtCore.QCalendar.System`, are also always available by name.

A :sip:ref:`~PyQt6.QtCore.QCalendar` value is immutable.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtCore.QDateTime`.
