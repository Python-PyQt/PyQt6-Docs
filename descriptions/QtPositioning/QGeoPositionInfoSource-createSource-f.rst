.. sip:method-description::
    :status: todo
    :pysig: a90472ce905a9009d71ea7fb9efba164
    :realsig: (const QString&, const QVariantMap&, QObject*)
    :digest: d71963341206dc9a2fa3d83e67a9619a

Creates and returns a position source with the given *parent*, by loading the plugin named *sourceName*.

Returns ``nullptr`` if the plugin cannot be found.

This method passes *parameters* to the factory to configure the source.
