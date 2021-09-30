.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: f2d567f243688f4954a4cec2ccab02e0

Sets the current audio file name to *fileName*.

When this property is set any current decoding is stopped, and any audio buffers are discarded.

You can only specify either a source filename or a source :sip:ref:`~PyQt6.QtCore.QIODevice`. Setting one will unset the other.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.source`.
