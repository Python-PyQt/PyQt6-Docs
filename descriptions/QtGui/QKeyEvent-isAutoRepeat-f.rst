.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: a636bd8b80bd4541843dcab6cc82ff1c

Returns ``true`` if this event comes from an auto-repeating key; returns ``false`` if it comes from an initial key press.

Note that if the event is a multiple-key compressed event that is partly due to auto-repeat, this function could return either true or false indeterminately.
