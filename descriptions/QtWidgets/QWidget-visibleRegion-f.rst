.. sip:method-description::
    :status: todo
    :pysig: 7b302619a1f8d21d9efa913403e8d56b
    :realsig: () const
    :digest: fd955651915d47735dadb70f6aa68e74

Returns the unobscured region where paint events can occur.

For visible widgets, this is an approximation of the area not covered by other widgets; otherwise, this is an empty region.

The :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` function calls this function if necessary, so in general you do not need to call it.
