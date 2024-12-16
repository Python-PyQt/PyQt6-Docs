.. sip:method-description::
    :status: todo
    :pysig: 82a33f5751e3ef405c358c8964b7e6df
    :realsig: (const QString&, const QVariantMap&, QObject*)
    :digest: 60745b236a3f0fe8fa633c8a94278726

Creates and returns a satellite source with the given *parent*, by loading the plugin named *sourceName*.

Returns ``nullptr`` if the plugin cannot be found.

This method passes *parameters* to the factory to configure the source.
