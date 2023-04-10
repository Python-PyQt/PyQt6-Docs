.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 30e3b0e1002de887fa8bec6057bbddb9

For a lightweight time representation whose :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC`, this returns the fixed offset from UTC that it describes. For any other time representation it returns 0, even if that time representation does have a constant offset from UTC.
