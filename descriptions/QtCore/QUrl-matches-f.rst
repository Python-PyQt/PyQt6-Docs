.. sip:method-description::
    :status: todo
    :pysig: 39fe1be1714659ceb8660d588974d585
    :realsig: (const QUrl&,QUrl::FormattingOptions) const
    :digest: 117a9164cc75ff97ae168fcd1cd3669d

Returns ``true`` if this URL and the given *url* are equal after applying *options* to both; otherwise returns ``false``.

This is equivalent to calling adjusted(options) on both URLs and comparing the resulting urls, but faster.
