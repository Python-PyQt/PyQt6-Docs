.. sip:method-description::
    :status: todo
    :pysig: f9cfd28ca6d3c7360a3087155446baa2
    :realsig: (int,QHeaderView::ResizeMode)
    :digest: 43746de133f1fcda15397a756eac27c9

Sets the constraints on how the section specified by *logicalIndex* in the header can be resized to those described by the given *mode*. The logical index should exist at the time this function is called.

**Note:** This setting will be ignored for the last section if the :sip:ref:`~PyQt6.QtWidgets.QHeaderView.stretchLastSection` property is set to true. This is the default for the horizontal headers provided by :sip:ref:`~PyQt6.QtWidgets.QTreeView`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setStretchLastSection`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.resizeContentsPrecision`.
