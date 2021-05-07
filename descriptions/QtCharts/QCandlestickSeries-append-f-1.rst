.. sip:method-description::
    :status: todo
    :pysig: 4086c82394817899a86d1f9ee7bb0702
    :realsig: (const QList<QCandlestickSet*>&)
    :digest: 7700c104a4952c03ada67b4c4499c8f5

Adds a list of candlestick items specified by *sets* to the series and takes ownership of it. If any of the items are null, already belong to the series, or appear in the list more than once, nothing is appended. Returns ``true`` if all items were appended successfully, ``false`` otherwise.
