.. sip:method-description::
    :status: todo
    :pysig: a4c85510175872bb6227eb5e62f4e503
    :realsig: (const uchar*,int,const char*)
    :digest: f5ed2e335576fdaa3b9c5b90ad86fb77

Loads an image from the first *len* bytes of the given binary *data*. Returns ``true`` if the image was successfully loaded; otherwise invalidates the image and returns ``false``.

The loader attempts to read the image using the specified *format*, e.g., PNG or JPG. If *format* is not specified (which is the default), the loader probes the file for a header to guess the file format.

.. seealso:: Reading and Writing Image Files.
