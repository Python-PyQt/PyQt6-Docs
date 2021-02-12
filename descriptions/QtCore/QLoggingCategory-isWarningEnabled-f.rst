.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 0b3a8b5f75e78d25feebb2fd0b5b2630

Returns ``true`` if warning messages should be shown for this category; ``false`` otherwise.

**Note:** The qCWarning() macro already does this check before executing any code. However, calling this method may be useful to avoid the expensive generation of data for debug output only.
