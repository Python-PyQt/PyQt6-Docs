.. sip:method-description::
    :status: todo
    :pysig: c504846bcb7eb244ce596264e7bacd8f
    :realsig: (QDate,QTime,const QTimeZone&)
    :digest: dadb07281b42561f20f5b642aad97309

Constructs a datetime with the given *date* and *time*, using the Time Zone specified by *timeZone*.

If *date* is valid and *time* is not, the time will be set to 00:00:00.

If *timeZone* is invalid then the datetime will be invalid.
