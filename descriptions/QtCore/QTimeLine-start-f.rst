.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 93d34c1f285e4b2d5aa712093dcea0da

Starts the timeline. :sip:ref:`~PyQt6.QtCore.QTimeLine` will enter Running state, and once it enters the event loop, it will update its current time, frame and value at regular intervals. The default interval is 40 ms (i.e., 25 times per second). You can change the update interval by calling :sip:ref:`~PyQt6.QtCore.QTimeLine.setUpdateInterval`.

The timeline will start from position 0, or the end if going backward. If you want to resume a stopped timeline without restarting, you can call :sip:ref:`~PyQt6.QtCore.QTimeLine.resume` instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeLine.resume`, :sip:ref:`~PyQt6.QtCore.QTimeLine.updateInterval`, :sip:ref:`~PyQt6.QtCore.QTimeLine.frameChanged`, :sip:ref:`~PyQt6.QtCore.QTimeLine.valueChanged`.
