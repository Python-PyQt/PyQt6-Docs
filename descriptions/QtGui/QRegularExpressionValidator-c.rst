.. sip:class-description::
    :status: todo
    :brief: Used to check a string against a regular expression
    :digest: 128a7b1848d8fd680453e3ea446144cb

The :sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator` class is used to check a string against a regular expression.

:sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator` uses a regular expression (regexp) to determine whether an input string is :sip:ref:`~PyQt6.QtGui.QValidator.State.Acceptable`, :sip:ref:`~PyQt6.QtGui.QValidator.State.Intermediate`, or :sip:ref:`~PyQt6.QtGui.QValidator.State.Invalid`. The regexp can either be supplied when the :sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator` is constructed, or at a later time.

If the regexp partially matches against the string, the result is considered :sip:ref:`~PyQt6.QtGui.QValidator.State.Intermediate`. For example, "" and "A" are :sip:ref:`~PyQt6.QtGui.QValidator.State.Intermediate` for the regexp **[A-Z][0-9]** (whereas "_" would be :sip:ref:`~PyQt6.QtGui.QValidator.State.Invalid`).

:sip:ref:`~PyQt6.QtGui.QRegularExpressionValidator` automatically wraps the regular expression in the ``\\A`` and ``\\z`` anchors; in other words, it always attempts to do an exact match.

Example of use:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qvalidator.py
    :lines: 125-130

Below we present some examples of validators. In practice they would normally be associated with a widget as in the example above.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qvalidator.py
    :lines: 134-164

.. seealso:: `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_, :sip:ref:`~PyQt6.QtGui.QIntValidator`, :sip:ref:`~PyQt6.QtGui.QDoubleValidator`.
