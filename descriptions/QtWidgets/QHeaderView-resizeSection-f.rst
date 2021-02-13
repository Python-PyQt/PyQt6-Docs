.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: bd30d2bb737b870904b85db034fed069

Resizes the section specified by *logicalIndex* to *size* measured in pixels. The size parameter must be a value larger or equal to zero. A size equal to zero is however not recommended. In that situation :sip:ref:`~PyQt6.QtWidgets.QHeaderView.hideSection` should be used instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionResized`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionSize`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.hideSection`.
