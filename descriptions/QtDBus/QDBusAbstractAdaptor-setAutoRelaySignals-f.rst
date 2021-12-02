.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 3a974ad92d4834db8329b64d904198e0

Toggles automatic signal relaying from the real object (see object()).

Automatic signal relaying consists of signal-to-signal connection of the signals on the parent that have the exact same method signature in both classes.

If *enable* is set to true, connect the signals; if set to false, disconnect all signals.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusAbstractAdaptor.autoRelaySignals`.
