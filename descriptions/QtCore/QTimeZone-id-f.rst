.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 183aaaadb36f36271c3f6198cc4ebe0a

Returns the IANA ID for the time zone.

IANA IDs are used on all platforms. On Windows these are translated from the Windows ID into the best match IANA ID for the time zone and territory.

This method is only available when feature ``timezone`` is enabled.
