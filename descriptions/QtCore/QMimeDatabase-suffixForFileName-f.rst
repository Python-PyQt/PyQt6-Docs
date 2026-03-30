.. sip:method-description::
    :status: todo
    :pysig: 558877a2dde966820eb6e4a9d974f77b
    :realsig: (const QString&) const
    :digest: 3b540591188fcfe6f5428037d23fabb1

Returns the suffix for the file *fileName*, as known by the MIME database.

This allows to pre-select "tar.bz2" for foo.tar.bz2, but still only "txt" for my.file.with.dots.txt.
