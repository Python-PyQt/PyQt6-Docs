.. sip:method-description::
    :status: todo
    :pysig: 21e64f79900eb5dec0c9e64f2dc51a93
    :realsig: (int, QWidget*, const QString&)
    :digest: e4bd2cdc17531b3f73528057620beb4a

Inserts a tab with the given *label* and *page* into the tab widget at the specified *index*, and returns the index of the inserted tab in the tab bar. Ownership of *page* is passed on to the :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

The label is displayed in the tab and may vary in appearance depending on the configuration of the tab widget.

If the tab's *label* contains an ampersand, the letter following the ampersand is used as a shortcut for the tab, e.g. if the label is "Bro&wse" then Alt+W becomes a shortcut which will move the focus to this tab.

If *index* is out of range, the tab is simply appended. Otherwise it is inserted at the specified position.

If the :sip:ref:`~PyQt6.QtWidgets.QTabWidget` was empty before this function is called, the new page becomes the current page. Inserting a new tab at an index less than or equal to the current index will increment the current index, but keep the current page.

**Note:** If you call insertTab() after show(), the layout system will try to adjust to the changes in its widgets hierarchy and may cause flicker. To prevent this, you can set the :sip:ref:`~PyQt6.QtWidgets.QWidget.updatesEnabled` property to false prior to changes; remember to set the property to true when the changes are done, making the widget receive paint events again.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget.addTab`.
