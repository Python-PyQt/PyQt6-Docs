.. sip:method-description::
    :status: todo
    :pysig: 9ed0de7ecb17b6432f6443fa97d3d34d
    :realsig: (const QCommandLineOption&)
    :digest: f6afad5a60b0d5774cc5b3f97a967368

Adds the option *option* to look for while parsing.

Returns ``true`` if adding the option was successful; otherwise returns ``false``.

Adding the option fails if there is no name attached to the option, or the option has a name that clashes with an option name added before.
