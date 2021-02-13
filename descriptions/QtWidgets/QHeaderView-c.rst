.. sip:class-description::
    :status: todo
    :brief: Header row or header column for item views
    :digest: ec196cf29f512665969c8c1925ad05e6

The :sip:ref:`~PyQt6.QtWidgets.QHeaderView` class provides a header row or header column for item views.

A :sip:ref:`~PyQt6.QtWidgets.QHeaderView` displays the headers used in item views such as the :sip:ref:`~PyQt6.QtWidgets.QTableView` and :sip:ref:`~PyQt6.QtWidgets.QTreeView` classes. It takes the place of Qt3's ``QHeader`` class previously used for the same purpose, but uses the Qt's model/view architecture for consistency with the item view classes.

The :sip:ref:`~PyQt6.QtWidgets.QHeaderView` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

The header gets the data for each section from the model using the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.headerData` function. You can set the data by using :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setHeaderData`.

Each header has an :sip:ref:`~PyQt6.QtWidgets.QHeaderView.orientation` and a number of sections, given by the :sip:ref:`~PyQt6.QtWidgets.QHeaderView.count` function. A section refers to a part of the header - either a row or a column, depending on the orientation.

Sections can be moved and resized using :sip:ref:`~PyQt6.QtWidgets.QHeaderView.moveSection` and :sip:ref:`~PyQt6.QtWidgets.QHeaderView.resizeSection`; they can also be hidden and shown with :sip:ref:`~PyQt6.QtWidgets.QHeaderView.hideSection` and :sip:ref:`~PyQt6.QtWidgets.QHeaderView.showSection`.

Each section of a header is described by a section ID, specified by its section(), and can be located at a particular :sip:ref:`~PyQt6.QtWidgets.QHeaderView.visualIndex` in the header. A section can have a sort indicator set with :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setSortIndicator`; this indicates whether the items in the associated item view will be sorted in the order given by the section.

For a horizontal header the section is equivalent to a column in the model, and for a vertical header the section is equivalent to a row in the model.

.. _qheaderview-moving-header-sections:

Moving Header Sections
----------------------

A header can be fixed in place, or made movable with :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setSectionsMovable`. It can be made clickable with :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setSectionsClickable`, and has resizing behavior in accordance with :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setSectionResizeMode`.

**Note:** Double-clicking on a header to resize a section only applies for visible rows.

A header will emit :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionMoved` if the user moves a section, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionResized` if the user resizes a section, and :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionClicked` as well as :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionHandleDoubleClicked` in response to mouse clicks. A header will also emit :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionCountChanged`.

You can identify a section using the :sip:ref:`~PyQt6.QtWidgets.QHeaderView.logicalIndex` and :sip:ref:`~PyQt6.QtWidgets.QHeaderView.logicalIndexAt` functions, or by its index position, using the :sip:ref:`~PyQt6.QtWidgets.QHeaderView.visualIndex` and :sip:ref:`~PyQt6.QtWidgets.QHeaderView.visualIndexAt` functions. The visual index will change if a section is moved, but the logical index will not change.

.. _qheaderview-appearance:

Appearance
----------

:sip:ref:`~PyQt6.QtWidgets.QTableWidget` and :sip:ref:`~PyQt6.QtWidgets.QTableView` create default headers. If you want the headers to be visible, you can use setVisible().

Not all :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`\ s will have an effect on a :sip:ref:`~PyQt6.QtWidgets.QHeaderView`. If you need to draw other roles, you can subclass :sip:ref:`~PyQt6.QtWidgets.QHeaderView` and reimplement :sip:ref:`~PyQt6.QtWidgets.QHeaderView.paintEvent`. :sip:ref:`~PyQt6.QtWidgets.QHeaderView` respects the following item data roles, unless they are in conflict with the style (which can happen for styles that follow the desktop theme):

:sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.TextAlignmentRole`, :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`, :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.FontRole`, :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DecorationRole`, :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.ForegroundRole`, and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.BackgroundRole`.

**Note:** Each header renders the data for each section itself, and does not rely on a delegate. As a result, calling a header's setItemDelegate() function will have no effect.

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtWidgets.QListView`, :sip:ref:`~PyQt6.QtWidgets.QTableView`, :sip:ref:`~PyQt6.QtWidgets.QTreeView`.
