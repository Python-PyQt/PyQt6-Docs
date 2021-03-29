.. sip:class-description::
    :status: todo
    :brief: Enables kinetic scrolling for any scrolling widget or graphics item
    :digest: 424143de3e7b516b4582ab44ace74b94

The :sip:ref:`~PyQt6.QtWidgets.QScroller` class enables kinetic scrolling for any scrolling widget or graphics item.

With kinetic scrolling, the user can push the widget in a given direction and it will continue to scroll in this direction until it is stopped either by the user or by friction. Aspects of inertia, friction and other physical concepts can be changed in order to fine-tune an intuitive user experience.

The :sip:ref:`~PyQt6.QtWidgets.QScroller` object is the object that stores the current position and scrolling speed and takes care of updates. :sip:ref:`~PyQt6.QtWidgets.QScroller` can be triggered by a flick gesture

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_widgets_util_qscroller.py
    :lines: 43-44

or directly like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_widgets_util_qscroller.py
    :lines: 48-50

The scrolled QObjects receive a :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent` whenever the scroller needs to update its geometry information and a :sip:ref:`~PyQt6.QtGui.QScrollEvent` whenever the content of the object should actually be scrolled.

The scroller uses the global :sip:ref:`~PyQt6.QtCore.QAbstractAnimation` timer to generate its QScrollEvents. This can be changed with :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties.ScrollMetric.FrameRate` on a per-\ :sip:ref:`~PyQt6.QtWidgets.QScroller` basis.

The `Dir View Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-dirview-example.html>`_ shows one way to use a :sip:ref:`~PyQt6.QtWidgets.QScroller` with a :sip:ref:`~PyQt6.QtWidgets.QTreeView`. An example in the ``scroller`` examples directory also demonstrates :sip:ref:`~PyQt6.QtWidgets.QScroller`.

Even though this kinetic scroller has a large number of settings available via :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties`, we recommend that you leave them all at their default, platform optimized values. Before changing them you can experiment with the ``plot`` example in the ``scroller`` examples directory.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QScrollEvent`, :sip:ref:`~PyQt6.QtGui.QScrollPrepareEvent`, :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties`.
