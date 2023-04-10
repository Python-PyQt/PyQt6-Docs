.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: eef73597bf7eeb694b2918569e302c70

Returns ``true`` if :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC` or :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC`.

When it is true, the time description does not change over time, such as having seasonal daylight-saving changes, as may happen for local time or a time zone. Knowing this may save the calling code to need for various other checks.
