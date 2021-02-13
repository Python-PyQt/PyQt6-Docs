.. sip:method-description::
    :status: todo
    :pysig: 18b89e220eebe5c40dbede2d92935137
    :realsig: (const QString&,const char*,int) const
    :digest: 98c603cd96501d435023912702bb9d9f

Saves the image to the file with the given *fileName*, using the given image file *format* and *quality* factor. If *format* is ``nullptr``, :sip:ref:`~PyQt6.QtGui.QImage` will attempt to guess the format by looking at *fileName*'s suffix.

The *quality* factor must be in the range 0 to 100 or -1. Specify 0 to obtain small compressed files, 100 for large uncompressed files, and -1 (the default) to use the default settings.

Returns ``true`` if the image was successfully saved; otherwise returns ``false``.

.. seealso:: Reading and Writing Image Files.
