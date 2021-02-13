.. sip:method-description::
    :status: todo
    :pysig: 845c88540cd788087bd7f4bc3a454b58
    :realsig: (QScrollBar*)
    :digest: efe4c88d3e93a40d466bf92054933f73

Replaces the existing vertical scroll bar with *scrollBar*, and sets all the former scroll bar's slider properties on the new scroll bar. The former scroll bar is then deleted.

:sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` already provides vertical and horizontal scroll bars by default. You can call this function to replace the default vertical scroll bar with your own custom scroll bar.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.verticalScrollBar`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.setHorizontalScrollBar`.
