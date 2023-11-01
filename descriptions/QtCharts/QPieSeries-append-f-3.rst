.. sip:method-description::
    :status: todo
    :pysig: aaf3413af5f9524dc30bb2241b931041
    :realsig: (const QString&, qreal)
    :digest: f42f20d8485b827d01c3e120c6aa32a4

Appends a single slice with the specified *value* and *label* to the series. Slice ownership is passed to the series. Returns null if *value* is ``NaN``, ``Inf``, or ``-Inf`` and adds nothing to the series.
