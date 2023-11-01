.. sip:method-description::
    :status: todo
    :pysig: 9006f4826ccc82d32e1b4efcf39f0c55
    :realsig: (const QString&, const QVariantMap&, QObject*)
    :digest: 60745b236a3f0fe8fa633c8a94278726

Creates and returns a satellite source with the given *parent*, by loading the plugin named *sourceName*.

Returns ``nullptr`` if the plugin cannot be found.

This method passes *parameters* to the factory to configure the source.
