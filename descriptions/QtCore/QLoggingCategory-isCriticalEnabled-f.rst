.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9fa8f43665a889b1046c46ec7609bd92

Returns ``true`` if critical messages should be shown for this category; ``false`` otherwise.

**Note:** The qCCritical() macro already does this check before executing any code. However, calling this method may be useful to avoid the expensive generation of data for debug output only.
