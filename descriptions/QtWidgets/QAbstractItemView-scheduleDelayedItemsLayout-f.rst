.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1430a8de2ffabdd4f28fb7c12eb2eca8

Schedules a layout of the items in the view to be executed when the event processing starts.

Even if  is called multiple times before events are processed, the view will only do the layout once.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.executeDelayedItemsLayout`.
