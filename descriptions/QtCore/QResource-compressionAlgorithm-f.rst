.. sip:method-description::
    :status: todo
    :pysig: 30c6eaf3eb72d7cf632737d4b28c3452
    :realsig: () const
    :digest: d02d1e480781ba8f1fb4fd277c219203

Returns the compression type that this resource is compressed with, if any. If it is not compressed, this function returns :sip:ref:`~PyQt6.QtCore.QResource.Compression.NoCompression`.

If this function returns :sip:ref:`~PyQt6.QtCore.QResource.Compression.ZlibCompression`, you may decompress the data using the :sip:ref:`~PyQt6.QtCore.qUncompress` function. Up until Qt 5.13, this was the only possible compression algorithm.

If this function returns :sip:ref:`~PyQt6.QtCore.QResource.Compression.ZstdCompression`, you need to use the Zstandard library functios (``<zstd.h> header). Qt does not provide a wrapper. See \l{http://facebook.github.io/zstd/zstd_manual.html}{Zstandard manual}. \sa data(), isFile()``
