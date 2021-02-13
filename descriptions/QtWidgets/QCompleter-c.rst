.. sip:class-description::
    :status: todo
    :brief: Completions based on an item model
    :digest: ec7d65edb8585d1100daedde83182f72

The :sip:ref:`~PyQt6.QtWidgets.QCompleter` class provides completions based on an item model.

You can use :sip:ref:`~PyQt6.QtWidgets.QCompleter` to provide auto completions in any Qt widget, such as :sip:ref:`~PyQt6.QtWidgets.QLineEdit` and `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_. When the user starts typing a word, :sip:ref:`~PyQt6.QtWidgets.QCompleter` suggests possible ways of completing the word, based on a word list. The word list is provided as a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`. (For simple applications, where the word list is static, you can pass a QStringList to :sip:ref:`~PyQt6.QtWidgets.QCompleter`'s constructor.)

.. _qcompleter-basic-usage:

Basic Usage
-----------

A :sip:ref:`~PyQt6.QtWidgets.QCompleter` is used typically with a :sip:ref:`~PyQt6.QtWidgets.QLineEdit` or `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_. For example, here's how to provide auto completions from a simple word list in a :sip:ref:`~PyQt6.QtWidgets.QLineEdit`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_util_qcompleter.py
    :lines: 54-61

A :sip:ref:`~PyQt6.QtGui.QFileSystemModel` can be used to provide auto completion of file names. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_util_qcompleter.py
    :lines: 66-68

To set the model on which :sip:ref:`~PyQt6.QtWidgets.QCompleter` should operate, call :sip:ref:`~PyQt6.QtWidgets.QCompleter.setModel`. By default, :sip:ref:`~PyQt6.QtWidgets.QCompleter` will attempt to match the :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionPrefix` (i.e., the word that the user has started typing) against the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` data stored in column 0 in the model case sensitively. This can be changed using :sip:ref:`~PyQt6.QtWidgets.QCompleter.setCompletionRole`, :sip:ref:`~PyQt6.QtWidgets.QCompleter.setCompletionColumn`, and :sip:ref:`~PyQt6.QtWidgets.QCompleter.setCaseSensitivity`.

If the model is sorted on the column and role that are used for completion, you can call :sip:ref:`~PyQt6.QtWidgets.QCompleter.setModelSorting` with either :sip:ref:`~PyQt6.QtWidgets.QCompleter.ModelSorting.CaseSensitivelySortedModel` or :sip:ref:`~PyQt6.QtWidgets.QCompleter.ModelSorting.CaseInsensitivelySortedModel` as the argument. On large models, this can lead to significant performance improvements, because :sip:ref:`~PyQt6.QtWidgets.QCompleter` can then use binary search instead of linear search. The binary search only works when the :sip:ref:`~PyQt6.QtWidgets.QCompleter.filterMode` is :sip:ref:`~PyQt6.QtCore.Qt.MatchFlags.MatchStartsWith`.

The model can be a :sip:ref:`~PyQt6.QtCore.QAbstractListModel`, a :sip:ref:`~PyQt6.QtCore.QAbstractTableModel`, or a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`. Completion on tree models is slightly more involved and is covered in the :ref:`qcompleter-handling-tree-models` section below.

The :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionMode` determines the mode used to provide completions to the user.

.. _qcompleter-iterating-through-completions:

Iterating Through Completions
-----------------------------

To retrieve a single candidate string, call :sip:ref:`~PyQt6.QtWidgets.QCompleter.setCompletionPrefix` with the text that needs to be completed and call :sip:ref:`~PyQt6.QtWidgets.QCompleter.currentCompletion`. You can iterate through the list of completions as below:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_util_qcompleter.py
    :lines: 73-74

:sip:ref:`~PyQt6.QtWidgets.QCompleter.completionCount` returns the total number of completions for the current prefix. :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionCount` should be avoided when possible, since it requires a scan of the entire model.

.. _qcompleter-the-completion-model:

The Completion Model
--------------------

:sip:ref:`~PyQt6.QtWidgets.QCompleter.completionModel` return a list model that contains all possible completions for the current completion prefix, in the order in which they appear in the model. This model can be used to display the current completions in a custom view. Calling :sip:ref:`~PyQt6.QtWidgets.QCompleter.setCompletionPrefix` automatically refreshes the completion model.

.. _qcompleter-handling-tree-models:

Handling Tree Models
--------------------

:sip:ref:`~PyQt6.QtWidgets.QCompleter` can look for completions in tree models, assuming that any item (or sub-item or sub-sub-item) can be unambiguously represented as a string by specifying the path to the item. The completion is then performed one level at a time.

Let's take the example of a user typing in a file system path. The model is a (hierarchical) :sip:ref:`~PyQt6.QtGui.QFileSystemModel`. The completion occurs for every element in the path. For example, if the current text is ``C:\Wind``, :sip:ref:`~PyQt6.QtWidgets.QCompleter` might suggest ``Windows`` to complete the current path element. Similarly, if the current text is ``C:\Windows\Sy``, :sip:ref:`~PyQt6.QtWidgets.QCompleter` might suggest ``System``.

For this kind of completion to work, :sip:ref:`~PyQt6.QtWidgets.QCompleter` needs to be able to split the path into a list of strings that are matched at each level. For ``C:\Windows\Sy``, it needs to be split as "C:", "Windows" and "Sy". The default implementation of :sip:ref:`~PyQt6.QtWidgets.QCompleter.splitPath`, splits the :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionPrefix` using :sip:ref:`~PyQt6.QtCore.QDir.separator` if the model is a :sip:ref:`~PyQt6.QtGui.QFileSystemModel`.

To provide completions, :sip:ref:`~PyQt6.QtWidgets.QCompleter` needs to know the path from an index. This is provided by :sip:ref:`~PyQt6.QtWidgets.QCompleter.pathFromIndex`. The default implementation of :sip:ref:`~PyQt6.QtWidgets.QCompleter.pathFromIndex`, returns the data for the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` for list models and the absolute file path if the mode is a :sip:ref:`~PyQt6.QtGui.QFileSystemModel`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_, `Completer Example <https://doc.qt.io/qt-6/qtwidgets-tools-completer-example.html>`_.
