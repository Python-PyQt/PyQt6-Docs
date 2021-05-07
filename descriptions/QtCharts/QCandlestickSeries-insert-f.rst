.. sip:method-description::
    :status: todo
    :pysig: 7024251e05a2f8619f26acbc23ca9840
    :realsig: (int,QCandlestickSet*)
    :digest: ae6856177493f3d4ec13f532c16f8971

Inserts the candlestick item specified by *set* to the series at the position specified by *index*. Takes ownership of the item. If the item is null or already belongs to the series, it is not inserted. Returns ``true`` if inserting succeeded, ``false`` otherwise.
