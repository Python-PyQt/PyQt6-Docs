.. sip:method-description::
    :status: todo
    :pysig: 58995d85e234d10a99bb87cdf1d979c9
    :realsig: (QWheelEvent*)
    :digest: c8abd32059a747e851ab1c639daeddf3

This event handler can be reimplemented in a subclass to receive wheel events for an item. The event information is provided by the *event* parameter.

The event is accepted by default, so it is not necessary to explicitly accept the event if you reimplement this function. If you don't accept the event, call ``event->ignore()``.
