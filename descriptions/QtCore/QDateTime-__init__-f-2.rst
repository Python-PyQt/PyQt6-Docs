.. sip:method-description::
    :status: todo
    :pysig: c504846bcb7eb244ce596264e7bacd8f
    :realsig: (QDate,QTime,const QTimeZone&)
    :digest: a585eb0210c8e8eefe05ca351f8ec201

Constructs a datetime with the given *date* and *time*, using the time representation described by *timeZone*.

If *date* is valid and *time* is not, the time will be set to midnight. If *timeZone* is invalid then the datetime will be invalid.
