.. sip:method-description::
    :status: todo
    :pysig: 99901c8d498bcfdef7e8e3814fe6ebb5
    :realsig: (const QString&, const QFont&, const QPaintDevice*)
    :digest: cacd781e94edbe40e02af4f70805f35d

Constructs a text layout to lay out the given *text* with the specified *font*.

All the metric and layout calculations will be done in terms of the paint device, *paintdevice*. If *paintdevice* is ``nullptr`` the calculations will be done in screen metrics.
