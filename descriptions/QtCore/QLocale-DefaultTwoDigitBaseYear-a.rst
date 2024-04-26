.. sip:attribute-description::
    :status: todo
    :digest: f8ff712898b12a1036c17958cd5c4af5

This variable holds The default start year of the century within which a format taking a two-digit year will select. The value of the constant is ``1900``..

Some locales use, particularly for :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat`, only the last two digits of the year. Proir to 6.7 the year 1900 was always used as a base year for such cases. Now various :sip:ref:`~PyQt6.QtCore.QLocale` and :sip:ref:`~PyQt6.QtCore.QDate` functions have the overloads that allow callers to specify the base year, and this constant is used as its default value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
