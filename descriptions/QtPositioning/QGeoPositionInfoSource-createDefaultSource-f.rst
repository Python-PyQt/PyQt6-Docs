.. sip:method-description::
    :status: todo
    :pysig: 29064034a2adac9bdf0994bebdd7ae5c
    :realsig: (QObject*)
    :digest: 79f0fd8cc0b212ed8fa12fab878804ec

Creates and returns a position source with the given *parent* that reads from the system's default sources of location data, or the plugin with the highest available priority.

Returns ``nullptr`` if the system has no default position source, no valid plugins could be found or the user does not have the permission to access the current position.
