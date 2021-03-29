.. sip:class-description::
    :status: todo
    :brief: Tab bar, e.g. for use in tabbed dialogs
    :digest: 021a2b704ce337407ccac88fa1d86fb5

The :sip:ref:`~PyQt6.QtWidgets.QTabBar` class provides a tab bar, e.g. for use in tabbed dialogs.

:sip:ref:`~PyQt6.QtWidgets.QTabBar` is straightforward to use; it draws the tabs using one of the predefined :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape`, and emits a signal when a tab is selected. It can be subclassed to tailor the look and feel. Qt also provides a ready-made :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

Each tab has a :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabText`, an optional :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabIcon`, an optional :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabToolTip`, optional :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabWhatsThis` and optional :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabData`. The tabs's attributes can be changed with :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabText`, :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabIcon`, :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabToolTip`, :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabWhatsThis` and :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabData`. Each tabs can be enabled or disabled individually with :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabEnabled`.

Each tab can display text in a distinct color. The current text color for a tab can be found with the :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabTextColor` function. Set the text color for a particular tab with :sip:ref:`~PyQt6.QtWidgets.QTabBar.setTabTextColor`.

Tabs are added using :sip:ref:`~PyQt6.QtWidgets.QTabBar.addTab`, or inserted at particular positions using :sip:ref:`~PyQt6.QtWidgets.QTabBar.insertTab`. The total number of tabs is given by :sip:ref:`~PyQt6.QtWidgets.QTabBar.count`. Tabs can be removed from the tab bar with :sip:ref:`~PyQt6.QtWidgets.QTabBar.removeTab`. Combining :sip:ref:`~PyQt6.QtWidgets.QTabBar.removeTab` and :sip:ref:`~PyQt6.QtWidgets.QTabBar.insertTab` allows you to move tabs to different positions.

The :sip:ref:`~PyQt6.QtWidgets.QTabBar.shape` property defines the tabs' appearance. The choice of shape is a matter of taste, although tab dialogs (for preferences and similar) invariably use :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape.RoundedNorth`. Tab controls in windows other than dialogs almost always use either :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape.RoundedSouth` or :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape.TriangularSouth`. Many spreadsheets and other tab controls in which all the pages are essentially similar use :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape.TriangularSouth`, whereas :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape.RoundedSouth` is used mostly when the pages are different (e.g. a multi-page tool palette). The default in :sip:ref:`~PyQt6.QtWidgets.QTabBar` is :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape.RoundedNorth`.

The most important part of :sip:ref:`~PyQt6.QtWidgets.QTabBar`'s API is the :sip:ref:`~PyQt6.QtWidgets.QTabBar.currentChanged` signal. This is emitted whenever the current tab changes (even at startup, when the current tab changes from 'none'). There is also a slot, :sip:ref:`~PyQt6.QtWidgets.QTabBar.setCurrentIndex`, which can be used to select a tab programmatically. The function :sip:ref:`~PyQt6.QtWidgets.QTabBar.currentIndex` returns the index of the current tab, :sip:ref:`~PyQt6.QtWidgets.QTabBar.count` holds the number of tabs.

:sip:ref:`~PyQt6.QtWidgets.QTabBar` creates automatic mnemonic keys in the manner of `QAbstractButton <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qabstractbutton>`_; e.g. if a tab's label is "&Graphics", Alt+G becomes a shortcut key for switching to that tab.

The following virtual functions may need to be reimplemented in order to tailor the look and feel or store extra data with each tab:

* :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabSizeHint` calcuates the size of a tab.

* :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabInserted` notifies that a new tab was added.

* :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabRemoved` notifies that a tab was removed.

* :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabLayoutChange` notifies that the tabs have been re-laid out.

* :sip:ref:`~PyQt6.QtWidgets.QTabBar.paintEvent` paints all tabs.

For subclasses, you might also need the :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabRect` functions which returns the visual geometry of a single tab.

+-------------------------------------+--------------------------------------------------------------------------------------+
| |image-fusion-tabbar-png|           | A tab bar shown in the `Fusion widget style <https://doc.qt.io/qt-6/gallery.html>`_. |
+-------------------------------------+--------------------------------------------------------------------------------------+
| |image-fusion-tabbar-truncated-png| | A truncated tab bar shown in the Fusion widget style.                                |
+-------------------------------------+--------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

.. |image-fusion-tabbar-png| image:: ../../../images/fusion-tabbar.png
.. |image-fusion-tabbar-truncated-png| image:: ../../../images/fusion-tabbar-truncated.png
