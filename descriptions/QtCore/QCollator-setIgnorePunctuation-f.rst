.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: f8ad74437bd9ddc219118c83e5726a18

If *on* is set to true, punctuation characters and symbols are ignored when determining sort order.

The default is locale dependent.

**Note:** This method is not currently supported if Qt is configured to not use ICU on Linux.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCollator.ignorePunctuation`.
