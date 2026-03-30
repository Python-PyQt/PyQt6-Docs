.. sip:method-description::
    :status: todo
    :pysig: 667ce776eb171df495d6573c12f5a573
    :realsig: (const QString&, const QString&, QNdefNfcTextRecord::Encoding)
    :digest: 7d63756f10d554880d8d9ae186d621bc

Attempts to add a new title record with title *text*, locale *locale* and encoding *encoding*. If the smart poster does not already contain a title record with locale *locale*, then the title record is added and the function returns ``true``. Otherwise ``false`` is returned.
