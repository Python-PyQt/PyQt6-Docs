.. sip:method-description::
    :status: todo
    :pysig: 8603e0898ac733ac27d59019fad14629
    :realsig: (QObject*)
    :digest: d4b2ff4cd2bda7b3238b5b7423d2b6a0

Creates and returns a source with the specified *parent* that reads from the system's default source of satellite update information, or the highest priority available plugin.

Returns ``nullptr`` if the system has no default satellite source, no valid plugins could be found or the user does not have the permission to access the satellite data.
