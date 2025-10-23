.. sip:method-description::
    :status: todo
    :pysig: 4a701eeb847c6efe98224fc34a30d1b0
    :realsig: (const QUrl&,QUrl::FormattingOptions) const
    :digest: 97f4504cabf04731a74431abe2c4252c

Returns ``true`` if this URL and the given *url* are equal after applying *options* to both; otherwise returns ``false``.

This is equivalent to calling :sip:ref:`~PyQt6.QtCore.QUrl.adjusted`\ (options) on both URLs and comparing the resulting urls, but faster.
