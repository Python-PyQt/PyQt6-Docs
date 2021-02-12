.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 79afb4c5986880ff5aeff4a73def93b2

If *paused* is true, the timeline is paused, causing :sip:ref:`~PyQt6.QtCore.QTimeLine` to enter Paused state. No updates will be signaled until either :sip:ref:`~PyQt6.QtCore.QTimeLine.start` or (false) is called. If *paused* is false, the timeline is resumed and continues where it left.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeLine.state`, :sip:ref:`~PyQt6.QtCore.QTimeLine.start`.
