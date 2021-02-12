.. sip:class-description::
    :status: todo
    :brief: Clock time functions
    :digest: 7992cdbb63b89a014278208877ca7b0f

The :sip:ref:`~PyQt6.QtCore.QTime` class provides clock time functions.

A :sip:ref:`~PyQt6.QtCore.QTime` object contains a clock time, which it can express as the numbers of hours, minutes, seconds, and milliseconds since midnight. It provides functions for comparing times and for manipulating a time by adding a number of milliseconds. :sip:ref:`~PyQt6.QtCore.QTime` objects should be passed by value rather than by reference to const; they simply package ``int``.

:sip:ref:`~PyQt6.QtCore.QTime` uses the 24-hour clock format; it has no concept of AM/PM. Unlike :sip:ref:`~PyQt6.QtCore.QDateTime`, :sip:ref:`~PyQt6.QtCore.QTime` knows nothing about time zones or daylight-saving time (DST).

A :sip:ref:`~PyQt6.QtCore.QTime` object is typically created either by giving the number of hours, minutes, seconds, and milliseconds explicitly, or by using the static function :sip:ref:`~PyQt6.QtCore.QTime.currentTime`, which creates a :sip:ref:`~PyQt6.QtCore.QTime` object that represents the system's local time.

The :sip:ref:`~PyQt6.QtCore.QTime.hour`, :sip:ref:`~PyQt6.QtCore.QTime.minute`, :sip:ref:`~PyQt6.QtCore.QTime.second`, and :sip:ref:`~PyQt6.QtCore.QTime.msec` functions provide access to the number of hours, minutes, seconds, and milliseconds of the time. The same information is provided in textual format by the :sip:ref:`~PyQt6.QtCore.QTime.toString` function.

The :sip:ref:`~PyQt6.QtCore.QTime.addSecs` and :sip:ref:`~PyQt6.QtCore.QTime.addMSecs` functions provide the time a given number of seconds or milliseconds later than a given time. Correspondingly, the number of seconds or milliseconds between two times can be found using :sip:ref:`~PyQt6.QtCore.QTime.secsTo` or :sip:ref:`~PyQt6.QtCore.QTime.msecsTo`.

:sip:ref:`~PyQt6.QtCore.QTime` provides a full set of operators to compare two :sip:ref:`~PyQt6.QtCore.QTime` objects; an earlier time is considered smaller than a later one; if A.\ :sip:ref:`~PyQt6.QtCore.QTime.msecsTo`\ (B) is positive, then A < B.

:sip:ref:`~PyQt6.QtCore.QTime` objects can also be created from a text representation using :sip:ref:`~PyQt6.QtCore.QTime.fromString` and converted to a string representation using :sip:ref:`~PyQt6.QtCore.QTime.toString`. All conversion to and from string formats is done using the C locale. For localized conversions, see :sip:ref:`~PyQt6.QtCore.QLocale`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtCore.QDateTime`.
