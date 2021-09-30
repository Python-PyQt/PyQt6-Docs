.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 19d89d6e1f61e59b30a0af204fd5cea3

Sets the *threshold* for archive bomb checks.

Some supported compression algorithms can, in a tiny compressed file, encode a spectacularly huge decompressed file. This is only possible if the decompressed content is extremely monotonous, which is seldom the case for real files being transmitted in good faith: files exercising such insanely high compression ratios are typically payloads of buffer-overrun attacks, or denial-of-service (by using up too much memory) attacks. Consequently, files that decompress to huge sizes, particularly from tiny compressed forms, are best rejected as suspected malware.

If a reply's decompressed size is bigger than this threshold (by default, 10 MiB, i.e. 10 \* 1024 \* 1024), Qt will check the compression ratio: if that is unreasonably large (40:1 for GZip and Deflate, or 100:1 for Brotli and ZStandard), the reply will be treated as an error. Setting the threshold to ``-1`` disables this check.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.decompressedSafetyCheckThreshold`.
