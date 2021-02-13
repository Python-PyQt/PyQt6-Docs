.. sip:class-description::
    :status: todo
    :brief: Groups actions together
    :digest: 875a906b579f5341f62ce5a5f57eaa4b

The :sip:ref:`~PyQt6.QtGui.QActionGroup` class groups actions together.

:sip:ref:`~PyQt6.QtGui.QActionGroup` is a base class for classes grouping classes inhheriting :sip:ref:`~PyQt6.QtGui.QAction` objects together.

In some situations it is useful to group :sip:ref:`~PyQt6.QtGui.QAction` objects together. For example, if you have a Left Align action, a Right Align action, a Justify action, and a Center action, only one of these actions should be active at any one time. One simple way of achieving this is to group the actions together in an action group, inheriting :sip:ref:`~PyQt6.QtGui.QActionGroup`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction`.
