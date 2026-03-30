.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: (const QRect&)
    :digest: a4ed3a0ef99bc0a8b30b999b1c08855c

The same as accept(), but also notifies that future moves will also be acceptable if they remain within the *rectangle* given on the widget. This can improve performance, but may also be ignored by the underlying system.

If the rectangle is empty, drag move events will be sent continuously. This is useful if the source is scrolling in a timer event.
