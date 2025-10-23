.. sip:enum-description::
    :status: todo
    :digest: 7d9d0ce2dc519dbaf944c266c8a0f72d

A timezone's name may vary seasonally to indicate whether it is using its standard offset from UTC or applying a daylight-saving adjustment to that offset. In such cases, it typically also has an overall name that applies to it regardless of season. When requesting the display name of a zone, this type identifies which of those names to use. In time zones that do not apply DST, all three values may return the same result.

This type is only available when feature ``timezone`` is enabled.
