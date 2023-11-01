.. sip:method-description::
    :status: todo
    :pysig: bf5e4049438b0497bad24e64ed05b425
    :realsig: (const QByteArray&, int)
    :digest: 1be4299e29ff3374bf16722f4bbbc74c

Compresses the *data* byte array and returns the compressed data in a new byte array.

The *compressionLevel* parameter specifies how much compression should be used. Valid values are between 0 and 9, with 9 corresponding to the greatest compression (i.e. smaller compressed data) at the cost of using a slower algorithm. Smaller values (8, 7, ..., 1) provide successively less compression at slightly faster speeds. The value 0 corresponds to no compression at all. The default value is -1, which specifies zlib's default compression.

.. seealso:: qUncompress(const QByteArray &data).
