.. sip:method-description::
    :status: todo
    :pysig: beae116e6e30ff65b5adb869b565e847
    :realsig: ()
    :digest: 1b4e87181eec00c69a444e5b1fc07c1e

Returns a :sip:ref:`~PyQt6.QtCore.QLocale` object initialized to the system locale.

The system locale may use system-specific sources for locale data, where available, otherwise falling back on :sip:ref:`~PyQt6.QtCore.QLocale`'s built-in database entry for the language, script and territory the system reports.

For example, on Windows and Mac, this locale will use the decimal/grouping characters and date/time formats specified in the system configuration panel.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.c`.
