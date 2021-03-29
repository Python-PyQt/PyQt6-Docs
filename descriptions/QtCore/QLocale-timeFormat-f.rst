.. sip:method-description::
    :status: todo
    :pysig: 47629bd086b1b98e7b6adf82de758d9b
    :realsig: (QLocale::FormatType) const
    :digest: b8a52f365873fa2cae0235789f4d691b

Returns the time format used for the current locale.

If *format* is :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat`, the format will be elaborate, otherwise it will be short. For example, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.LongFormat` for the ``en_US`` locale is ``h:mm:ss AP t``, :sip:ref:`~PyQt6.QtCore.QLocale.FormatType.ShortFormat` is ``h:mm AP``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.toString`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`.
