.. sip:method-description::
    :status: todo
    :pysig: a70013009e14d17cf8a7e7f053a43b3d
    :realsig: (QCandlestickSet*)
    :digest: c6a595d561f3de877f77d4ebdebc80b0

Takes a single candlestick item, specified by *set*, from the series. Does not delete the item. Returns ``true`` if the take operation was successful, ``false`` otherwise.

**Note:** The series remains the item's parent object. You must set the parent object to take full ownership.
