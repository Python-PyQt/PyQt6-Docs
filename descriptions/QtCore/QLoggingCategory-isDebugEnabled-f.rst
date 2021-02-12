.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: e39764363b58aadaf0419e32f630ebc6

Returns ``true`` if debug messages should be shown for this category; ``false`` otherwise.

**Note:** The qCDebug() macro already does this check before running any code. However, calling this method may be useful to avoid the expensive generation of data for debug output only.
