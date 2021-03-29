.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 61802eed664bc2fcbe75a2658b1ddd1f

Returns ``true`` if informational messages should be shown for this category; ``false`` otherwise.

**Note:** The qCInfo() macro already does this check before executing any code. However, calling this method may be useful to avoid the expensive generation of data for debug output only.
