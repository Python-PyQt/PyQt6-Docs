.. sip:method-description::
    :status: todo
    :pysig: 4086c82394817899a86d1f9ee7bb0702
    :realsig: (const QList<QCandlestickSet*>&)
    :digest: 5fd1d334a976839fb4684d7567f5e6da

Removes a list of candlestick items specified by *sets* from the series. If any of the items are null, were already removed from the series, or appear in the list more than once, nothing is removed. Returns ``true`` if all items were removed successfully, ``false`` otherwise.
