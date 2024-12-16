.. sip:method-description::
    :status: todo
    :pysig: ed2b54e51a824966b796909d3e32f171
    :realsig: (const QList<QBarSet*>&)
    :digest: 8686b32f1df94539bc802f74e57ac089

Adds a list of bar sets specified by *sets* to a bar series and takes ownership of the sets. Returns ``true`` if all sets were appended successfully. If any of the sets is null or was previously appended to the series, nothing is appended and this function returns ``false``. If any of the sets appears in the list more than once, nothing is appended and this function returns ``false``.
