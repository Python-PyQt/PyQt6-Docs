.. sip:enum-member-description::
    :status: todo
    :value: 9
    :digest: 4ec9161134ce2fa8ba1f8f88236227ab

`ISO 8601 <https://doc.qt.io/qt-6/http://www.iso.org/iso/catalogue_detail?csnumber=40874>`_ extended format: uses ``yyyy-MM-dd`` for dates, ``HH:mm:ss.zzz`` for times or ``yyyy-MM-ddTHH:mm:ss.zzz`` (e.g. 2017-07-24T15:46:29.739) for combined dates and times, optionally with a time-zone suffix (Z for UTC otherwise an offset as ±HH:mm) where appropriate. When parsed, a single space, ``' '``, may be used in place of the ``'T'`` separator between date and time; no other spacing characters are permitted. This format also accepts ``HH:mm`` and plain ``HH`` formats for the time part, either of which may include a fractional part, ``HH:mm.zzz`` or ``HH.zzz``, applied to the last field present (hour or minute).
