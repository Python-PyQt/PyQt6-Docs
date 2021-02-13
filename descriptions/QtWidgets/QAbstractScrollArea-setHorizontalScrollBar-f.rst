.. sip:method-description::
    :status: todo
    :pysig: 845c88540cd788087bd7f4bc3a454b58
    :realsig: (QScrollBar*)
    :digest: da5c3f58f17dc91c089838580409cd3a

Replaces the existing horizontal scroll bar with *scrollBar*, and sets all the former scroll bar's slider properties on the new scroll bar. The former scroll bar is then deleted.

:sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` already provides horizontal and vertical scroll bars by default. You can call this function to replace the default horizontal scroll bar with your own custom scroll bar.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBar`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.setVerticalScrollBar`.
