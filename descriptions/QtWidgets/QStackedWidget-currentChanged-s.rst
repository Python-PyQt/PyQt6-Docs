.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: e863dd233497fc428785b88a2bf557a9

This signal is emitted whenever the current widget changes.

The parameter holds the *index* of the new current widget, or -1 if there isn't a new one (for example, if there are no widgets in the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.currentWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.setCurrentWidget`.
