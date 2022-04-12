.. sip:method-description::
    :status: todo
    :pysig: 30c6eaf3eb72d7cf632737d4b28c3452
    :realsig: () const
    :digest: 2d0019aef84d99ac8218d2f9aee1ec9c

Returns the compression type that this resource is compressed with, if any. If it is not compressed, this function returns :sip:ref:`~PyQt6.QtCore.QResource.Compression.NoCompression`.

If this function returns :sip:ref:`~PyQt6.QtCore.QResource.Compression.ZlibCompression`, you may decompress the data using the :sip:ref:`~PyQt6.QtCore.qUncompress` function. Up until Qt 5.13, this was the only possible compression algorithm.

If this function returns :sip:ref:`~PyQt6.QtCore.QResource.Compression.ZstdCompression`, you need to use the Zstandard library functions (``<zstd.h>`` header). Qt does not provide a wrapper.

See `Zstandard manual <http://facebook.github.io/zstd/zstd_manual.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QResource.data`, :sip:ref:`~PyQt6.QtCore.QResource.isFile`.
