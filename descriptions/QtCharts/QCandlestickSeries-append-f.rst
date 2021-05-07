.. sip:method-description::
    :status: todo
    :pysig: a70013009e14d17cf8a7e7f053a43b3d
    :realsig: (QCandlestickSet*)
    :digest: 44455c0c471b1a6e60c2e1006e2f52d8

Adds a single candlestick item specified by *set* to the series and takes ownership of it. If the item is null or it is already in the series, it is not appended. Returns ``true`` if appending succeeded, ``false`` otherwise.
