.. sip:method-description::
    :status: todo
    :pysig: d68a2bc272eafa2869d310e61eeccbbc
    :realsig: (const QSize&,QIcon::Mode,QIcon::State) const
    :digest: ead4409cc0f97f249e379a5aadaf053c

Returns a pixmap with the requested *size*, *mode*, and *state*, generating one if necessary. The pixmap might be smaller than requested, but never larger, unless the device-pixel ratio of the returned pixmap is larger than 1.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.actualSize`, :sip:ref:`~PyQt6.QtGui.QIcon.paint`.
