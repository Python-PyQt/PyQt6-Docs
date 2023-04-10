.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 33be838017a2ad2b806470b0f82e60f1

Sets the application's badge to *number*.

Useful for providing feedback to the user about the number of unread messages or similar.

The badge will be overlaid on the application's icon in the Dock on macOS, the home screen icon on iOS, or the task bar on Windows.

If the number is outside the range supported by the platform, the number will be clamped to the supported range. If the number does not fit within the badge, the number may be visually elided.

Setting the number to 0 will clear the badge.

.. seealso:: applicationName.
