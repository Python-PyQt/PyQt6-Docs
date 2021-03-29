.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 6293677d5c538ada66cc479135f4e0f8

If *movable* is true, the header sections may be moved by the user; otherwise they are fixed in place.

When used in combination with :sip:ref:`~PyQt6.QtWidgets.QTreeView`, the first column is not movable (since it contains the tree structure), by default. You can make it movable with :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setFirstSectionMovable`\ (true).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionsMovable`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.sectionMoved`, :sip:ref:`~PyQt6.QtWidgets.QHeaderView.setFirstSectionMovable`.
