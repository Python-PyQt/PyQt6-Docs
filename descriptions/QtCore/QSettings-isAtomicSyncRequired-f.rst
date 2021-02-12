.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6b416c81c53bcbd43f938bfa39efac23

Returns ``true`` if :sip:ref:`~PyQt6.QtCore.QSettings` is only allowed to perform atomic saving and reloading (synchronization) of the settings. Returns ``false`` if it is allowed to save the settings contents directly to the configuration file.

The default is ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.setAtomicSyncRequired`, :sip:ref:`~PyQt6.QtCore.QSaveFile`.
