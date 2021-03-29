.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8a5a7afe55621f069e190ff49bd4ad64

Resumes the timeline from the current time. :sip:ref:`~PyQt6.QtCore.QTimeLine` will reenter Running state, and once it enters the event loop, it will update its current time, frame and value at regular intervals.

In contrast to :sip:ref:`~PyQt6.QtCore.QTimeLine.start`, this function does not restart the timeline before it resumes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeLine.start`, :sip:ref:`~PyQt6.QtCore.QTimeLine.updateInterval`, :sip:ref:`~PyQt6.QtCore.QTimeLine.frameChanged`, :sip:ref:`~PyQt6.QtCore.QTimeLine.valueChanged`.
