.. sip:method-description::
    :status: todo
    :pysig: 33c2742a69f0e5964f96b6df91b77fe0
    :realsig: (const QString&, const QVariantMap&)
    :digest: 694827b6d765d200a74c37495e4f75aa

Sets the engine used by this :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech` object to *engine*, passing *params* through to the engine constructor.

Returns whether *engine* could be set successfully.

Which key/value pairs in *params* are supported depends on the engine. See `the engine documentation <https://doc.qt.io/qt-6/qttexttospeech-engines.html>`_ for details. Unsupported entries will be ignored.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.engine`.
