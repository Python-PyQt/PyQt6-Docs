.. sip:method-description::
    :status: todo
    :pysig: 0fb2059ab3e864b364165f3633e81d6d
    :realsig: (QGesture*)
    :digest: 1e822da1ae1ac3246fb8a29a8d84e56e

This function is called by Qt to reset a given *gesture*.

Reimplement this function to implement additional requirements for custom :sip:ref:`~PyQt6.QtWidgets.QGesture` objects. This may be necessary if you implement a custom :sip:ref:`~PyQt6.QtWidgets.QGesture` whose properties need special handling when the gesture is reset.
