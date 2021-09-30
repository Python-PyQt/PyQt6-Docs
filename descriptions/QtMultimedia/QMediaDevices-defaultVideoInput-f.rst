.. sip:method-description::
    :status: todo
    :pysig: e5a820bebe2b30ef7a49b1d75ab8c003
    :realsig: ()
    :digest: e9322aee8067a2d1bfab6b3962fd4292

Returns the default camera on the system.

/note The returned object should be checked using isNull() before being used, in case there is no default camera or no cameras at all.

The default device can change during the runtime of the application. The :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.videoInputsChanged` signal is emitted in that case.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices.videoInputs`.
