.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: 4c4922376d2f07f670d13af2a3d58b95

Loads a text-to-speech engine from a plug-in that uses the default engine plug-in and constructs a :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech` object as the child of *parent*.

The default engine is platform-specific.

If the engine initializes correctly, then the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` of the engine will change to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Ready`; note that this might happen asynchronously. If the plugin fails to load, then :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` will be set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Error`.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.availableEngines`.
