.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 96c7da5b344a71be1d847bd613f8c81b

Returns true if the property needs a change notifier signal for bindings to remain upto date, false otherwise.

Some properties, such as attached properties or those whose value never changes, do not require a change notifier.
