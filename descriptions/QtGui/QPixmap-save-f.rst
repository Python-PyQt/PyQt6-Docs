.. sip:method-description::
    :status: todo
    :pysig: 7690ac7336ace8c4a0f8a078d432b865
    :realsig: (const QString&, const char*, int) const
    :digest: 4cd920336294fd2683293c63859e8d19

Saves the pixmap to the file with the given *fileName* using the specified image file *format* and *quality* factor. Returns ``true`` if successful; otherwise returns ``false``.

The *quality* factor must be in the range [0,100] or -1. Specify 0 to obtain small compressed files, 100 for large uncompressed files, and -1 to use the default settings.

If *format* is ``nullptr``, an image format will be chosen from *fileName*'s suffix.

.. seealso:: Reading and Writing Image Files.
