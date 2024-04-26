.. sip:method-description::
    :status: todo
    :pysig: be4cf29ba73c5c1c9c66cbed303bedcd
    :realsig: (const QString&,QObject*)
    :digest: f2f33f2cf2082fa41d3a04f7e930093f

Loads a text-to-speech engine from a plug-in that matches parameter *engine* and constructs a :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech` object as the child of *parent*.

If *engine* is empty, the default engine plug-in is used. The default engine is platform-specific.

If the engine initializes correctly, the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` of the engine will be set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Ready`. If the plugin fails to load, or if the engine fails to initialize, the engine's :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` will be set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Error`.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.availableEngines`.
