.. sip:method-description::
    :status: todo
    :pysig: d151ab632409f24bb0c072de6bfdd84e
    :realsig: (const QString&,const QVariantMap&,QObject*)
    :digest: 4e0ae04116f6bca055da2dd2c03003a8

Loads a text-to-speech engine from a plug-in that matches parameter *engine* and constructs a :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech` object as the child of *parent*, passing *params* through to the engine.

If *engine* is empty, the default engine plug-in is used. The default engine is platform-specific. Which key/value pairs in *params* are supported depends on the engine. See `the engine documentation <https://doc.qt.io/qt-6/qttexttospeech-engines.html>`_ for details. Unsupported entries will be ignored.

If the engine initializes correctly, the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` of the engine will be set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Ready`. If the plugin fails to load, or if the engine fails to initialize, the engine's :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` will be set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Error`.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.availableEngines`.
