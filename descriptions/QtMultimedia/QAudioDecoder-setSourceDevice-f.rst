.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: 4f490bef9c0377b368bb522ea635e23c

Sets the current audio :sip:ref:`~PyQt6.QtCore.QIODevice` to *device*.

When this property is set any current decoding is stopped, and any audio buffers are discarded.

You can only specify either a source filename or a source :sip:ref:`~PyQt6.QtCore.QIODevice`. Setting one will unset the other.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.sourceDevice`.
