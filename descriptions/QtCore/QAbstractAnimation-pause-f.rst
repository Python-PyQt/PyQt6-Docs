.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5b7a1c57da442bc0088d1144215d66f6

Pauses the animation. When the animation is paused, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.state` returns Paused. The value of :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.currentTime` will remain unchanged until :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.resume` or :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.start` is called. If you want to continue from the current time, call :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.resume`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.start`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.state`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.resume`.
