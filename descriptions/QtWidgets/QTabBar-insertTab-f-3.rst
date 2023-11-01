.. sip:method-description::
    :status: todo
    :pysig: 84d5af5271becaa22acbcf4576d2df7b
    :realsig: (int, const QIcon&, const QString&)
    :digest: e8d6fcf953abb74c358f9b35f11fa076

This is an overloaded function.

Inserts a new tab with icon *icon* and text *text* at position *index*. If *index* is out of range, the new tab is appended. Returns the new tab's index.

If the :sip:ref:`~PyQt6.QtWidgets.QTabBar` was empty before this function is called, the inserted tab becomes the current tab.

Inserting a new tab at an index less than or equal to the current index will increment the current index, but keep the current tab.
