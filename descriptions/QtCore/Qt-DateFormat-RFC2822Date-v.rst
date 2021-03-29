.. sip:enum-member-description::
    :status: todo
    :value: 8
    :digest: 04d5624167078cc5dd711b4b8763dc9b

RFC 2822, RFC 850 and RFC 1036 format: when converting dates to string form, format ``dd MMM yyyy`` is used, for times the format is ``HH:mm:ss``. For combined date and time, these are combined as ``dd MMM yyyy HH:mm:ss ±tzoff`` (omitting the optional leading day of the week from the first format recognized). When reading from a string either ``[ddd,] dd MMM yyyy [HH:mm[:ss]][ ±tzoff]`` or ``ddd MMM dd[ HH:mm:ss] yyyy[ ±tzoff]`` will be recognized for combined dates and times, where ``tzoff`` is a timezone offset in ``HHmm`` format. Arbitrary spacing may appear before or after the text and any non-empty spacing may replace the spaces in this format. For dates and times separately, the same formats are matched and the unwanted parts are ignored. In particular, note that a time is not recognized without an accompanying date.
