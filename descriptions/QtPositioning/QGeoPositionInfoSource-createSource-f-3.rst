.. sip:method-description::
    :status: todo
    :pysig: 1e363327716bbd68dda508eaa33b2020
    :realsig: (const QString&, const QVariantMap&, QObject*)
    :digest: d71963341206dc9a2fa3d83e67a9619a

Creates and returns a position source with the given *parent*, by loading the plugin named *sourceName*.

Returns ``nullptr`` if the plugin cannot be found.

This method passes *parameters* to the factory to configure the source.
