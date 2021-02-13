.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: f5118cac10a8d5373dd78951a5955484

Returns ``true`` if this item filters child events (i.e., all events intended for any of its children are instead sent to this item); otherwise, false is returned.

The default value is false; child events are not filtered.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setFiltersChildEvents`.
