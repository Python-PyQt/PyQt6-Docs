.. sip:method-description::
    :status: todo
    :pysig: 90172dcf16d50c84f946cd69ad1acd11
    :realsig: (const QSize&,QIcon::Mode,QIcon::State)
    :digest: 10348c74cf1328b61bb6238c1e201ab6

Returns the actual size of the icon the engine provides for the requested *size*, *mode* and *state*. The default implementation returns the given *size*.

The returned size is in device-independent pixels (This is relevant for high-dpi pixmaps).
