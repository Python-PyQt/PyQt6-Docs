.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: c6a75c500f54272789d9554b2d7403cd

Sets the ordering requirements of the filter. If *on* is ``true``, the filter will only match if the order of records in the filter matches the order of the records in the NDEF message. If *on* is ``false``, the order of the records is not taken into account when matching.

By default record order is not taken into account.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNdefFilter.orderMatch`.
