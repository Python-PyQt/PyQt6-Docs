.. sip:method-description::
    :status: todo
    :pysig: 2a982ecede56b474bbafcc0c5266ddec
    :realsig: (const QVariantMap&,QObject*)
    :digest: 42d2f1d606b6a7d5da8496e886cd536e

Creates and returns a satellite source with the given *parent* that reads from the system's default sources of satellite data, or the plugin with the highest available priority.

Returns ``nullptr`` if the system has no default satellite source, no valid plugins could be found or the user does not have the permission to access the satellite information.

This method passes *parameters* to the factory to configure the source.
