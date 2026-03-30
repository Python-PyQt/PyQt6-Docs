.. sip:method-description::
    :status: todo
    :pysig: 3986fcad7bb3dd968f57ab602d0385f6
    :realsig: (int, QWidget*, const QIcon&, const QString&)
    :digest: 8615ac5d8978116fcdb26d59c4431abe

Inserts a tab with the given *label*, *page*, and *icon* into the tab widget at the specified *index*, and returns the index of the inserted tab in the tab bar. Ownership of *page* is passed on to the :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

This function is the same as :sip:ref:`~PyQt6.QtWidgets.QTabWidget.insertTab`, but with an additional *icon*.
