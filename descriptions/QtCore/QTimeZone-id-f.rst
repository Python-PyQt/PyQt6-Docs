.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 6b884775f24cfe0a09caf8e7465395c0

Returns the IANA ID for the time zone.

IANA IDs are used on all platforms. On Windows these are translated from the Windows ID into the best match IANA ID for the time zone and territory.

If this timezone instance was not constructed from an IANA ID, its ID is determined by how it was constructed. In most cases, the ID passed when constructing the instance is used. (The constructor for a custom zone uses the ID it is passed, which must not be an IANA ID.) There are two exceptions.

* Instances constructed by passing only a UTC offset in seconds have no ID passed when constructing.

* The constructor taking only an IANA ID will also accept some UTC-offset IDs that are not in fact IANA IDs: its handling of these is equivalent to passing the corresponding offset in seconds, as for the first exception.

In the two exceptional cases, if there is an IANA UTC-offset zone with the specified offset, the instance constructed uses that IANA zone's ID, even though this may differ from the (non-IANA) UTC-offset ID passed to the constructor. Otherwise, the instance uses an ID synthesized from its offset, with the form UTC±hh:mm:ss, omitting any trailing :00 for zero seconds or minutes. Again, this may differ from the UTC-offset ID passed to the constructor.

This method is only available when feature ``timezone`` is enabled.
