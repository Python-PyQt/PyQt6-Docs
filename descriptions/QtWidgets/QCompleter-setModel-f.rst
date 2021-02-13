.. sip:method-description::
    :status: todo
    :pysig: b1398307ea89da5fe868fb6740f9bc55
    :realsig: (QAbstractItemModel*)
    :digest: be9523832e0d3c7f3599bf76d93face6

Sets the model which provides completions to *model*. The *model* can be list model or a tree model. If a model has been already previously set and it has the :sip:ref:`~PyQt6.QtWidgets.QCompleter` as its parent, it is deleted.

For convenience, if *model* is a :sip:ref:`~PyQt6.QtGui.QFileSystemModel`, :sip:ref:`~PyQt6.QtWidgets.QCompleter` switches its :sip:ref:`~PyQt6.QtWidgets.QCompleter.caseSensitivity` to :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity.CaseInsensitive` on Windows and :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity.CaseSensitive` on other platforms.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionModel`, :sip:ref:`~PyQt6.QtWidgets.QCompleter.modelSorting`, :ref:`qcompleter-handling-tree-models`.
