.. sip:signal-description::
    :status: todo
    :pysig: 6d06c328764df1e8076a52609ba73267
    :realsig: (QTextToSpeech::ErrorReason, const QString&)
    :digest: 5d03de2a76e4fad31722e56e5b05029f

This signal is emitted after an error occurred and the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` has been set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Error`. The *reason* parameter specifies the type of error, and the *errorString* provides a human-readable error description.

:sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason` is not a registered metatype, so for queued connections, you will have to register it with Q_DECLARE_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.errorReason`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.errorString`, `Creating Custom Qt Types <https://doc.qt.io/qt-6/custom-types.html>`_.
