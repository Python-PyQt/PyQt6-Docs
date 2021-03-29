.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 3e8c4701073f000b98b674f0a64be500

If *enabled* is true, this item is set to filter all events for all its children (i.e., all events intented for any of its children are instead sent to this item); otherwise, if *enabled* is false, this item will only handle its own events. The default value is false.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.filtersChildEvents`.
