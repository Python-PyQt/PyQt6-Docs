.. sip:method-description::
    :status: todo
    :pysig: 332e973ea039e2123fc4cae244a9717a
    :realsig: (qint64,int,QLocale::DataSizeFormats) const
    :digest: 8f8af9df9664f68e7f30b1e0cea2f21f

Converts a size in bytes to a human-readable localized string, comprising a number and a quantified unit. The quantifier is chosen such that the number is at least one, and as small as possible. For example if *bytes* is 16384, *precision* is 2, and *format* is :sip:ref:`~PyQt6.QtCore.QLocale.DataSizeFormats.DataSizeIecFormat` (the default), this function returns "16.00 KiB"; for 1330409069609 bytes it returns "1.21 GiB"; and so on. If *format* is :sip:ref:`~PyQt6.QtCore.QLocale.DataSizeFormats.DataSizeIecFormat` or :sip:ref:`~PyQt6.QtCore.QLocale.DataSizeFormats.DataSizeTraditionalFormat`, the given number of bytes is divided by a power of 1024, with result less than 1024; for :sip:ref:`~PyQt6.QtCore.QLocale.DataSizeFormats.DataSizeSIFormat`, it is divided by a power of 1000, with result less than 1000. ``DataSizeIecFormat`` uses the new IEC standard quantifiers Ki, Mi and so on, whereas ``DataSizeSIFormat`` uses the older SI quantifiers k, M, etc., and ``DataSizeTraditionalFormat`` abuses them.
