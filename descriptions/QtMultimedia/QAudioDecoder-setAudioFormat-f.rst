.. sip:method-description::
    :status: todo
    :pysig: 394200b40df23d07efe9586de9a39591
    :realsig: (const QAudioFormat&)
    :digest: c0a6af8f509654b12132c3a996e89ab1

Set the desired audio format for decoded samples to *format*.

This property can only be set while the decoder is stopped. Setting this property at other times will be ignored.

If the decoder does not support this format, :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.error` will be set to ``FormatError``.

If you do not specify a format, the format of the decoded audio itself will be used. Otherwise, some format conversion will be applied.

If you wish to reset the decoded format to that of the original audio file, you can specify an invalid *format*.

**Warning:** Setting a desired audio format is not yet supported on Android.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.audioFormat`.
