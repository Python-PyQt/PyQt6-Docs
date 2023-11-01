.. sip:class-description::
    :status: todo
    :brief: List or icon view onto a model
    :digest: e9c806c12c48e0aa2b0f039d2f424174

The :sip:ref:`~PyQt6.QtWidgets.QListView` class provides a list or icon view onto a model.

.. image:: ../../../images/windows-listview.png

A :sip:ref:`~PyQt6.QtWidgets.QListView` presents items stored in a model, either as a simple non-hierarchical list, or as a collection of icons. This class is used to provide lists and icon views that were previously provided by the ``QListBox`` and ``QIconView`` classes, but using the more flexible approach provided by Qt's model/view architecture.

The :sip:ref:`~PyQt6.QtWidgets.QListView` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

This view does not display horizontal or vertical headers; to display a list of items with a horizontal header, use :sip:ref:`~PyQt6.QtWidgets.QTreeView` instead.

:sip:ref:`~PyQt6.QtWidgets.QListView` implements the interfaces defined by the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` class to allow it to display data provided by models derived from the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` class.

Items in a list view can be displayed using one of two view modes: In :sip:ref:`~PyQt6.QtWidgets.QListView.ViewMode.ListMode`, the items are displayed in the form of a simple list; in :sip:ref:`~PyQt6.QtWidgets.QListView.ViewMode.IconMode`, the list view takes the form of an *icon view* in which the items are displayed with icons like files in a file manager. By default, the list view is in :sip:ref:`~PyQt6.QtWidgets.QListView.ViewMode.ListMode`. To change the view mode, use the :sip:ref:`~PyQt6.QtWidgets.QListView.setViewMode` function, and to determine the current view mode, use :sip:ref:`~PyQt6.QtWidgets.QListView.viewMode`.

Items in these views are laid out in the direction specified by the :sip:ref:`~PyQt6.QtWidgets.QListView.flow` of the list view. The items may be fixed in place, or allowed to move, depending on the view's :sip:ref:`~PyQt6.QtWidgets.QListView.movement` state.

If the items in the model cannot be completely laid out in the direction of flow, they can be wrapped at the boundary of the view widget; this depends on :sip:ref:`~PyQt6.QtWidgets.QListView.isWrapping`. This property is useful when the items are being represented by an icon view.

The :sip:ref:`~PyQt6.QtWidgets.QListView.resizeMode` and :sip:ref:`~PyQt6.QtWidgets.QListView.layoutMode` govern how and when the items are laid out. Items are spaced according to their :sip:ref:`~PyQt6.QtWidgets.QListView.spacing`, and can exist within a notional grid of size specified by :sip:ref:`~PyQt6.QtWidgets.QListView.gridSize`. The items can be rendered as large or small icons depending on their iconSize().

.. _qlistview-improving-performance:

Improving Performance
---------------------

It is possible to give the view hints about the data it is handling in order to improve its performance when displaying large numbers of items. One approach that can be taken for views that are intended to display items with equal sizes is to set the :sip:ref:`~PyQt6.QtWidgets.QListView.uniformItemSizes` property to true.

.. seealso:: `View Classes <https://doc.qt.io/qt-6/model-view-programming.html#view-classes>`_, :sip:ref:`~PyQt6.QtWidgets.QTreeView`, :sip:ref:`~PyQt6.QtWidgets.QTableView`, :sip:ref:`~PyQt6.QtWidgets.QListWidget`.
