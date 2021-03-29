.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 251102b01996e9e4b45144c6652f9338

This function resends the :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent`. Calling  triggers a :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent` from the scroller. This allows the receiver to re-set content position and content size while scrolling. Calling this function while in the Inactive state is useless as the prepare event is sent again before scrolling starts.
