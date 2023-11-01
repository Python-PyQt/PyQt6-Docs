.. sip:class-description::
    :status: todo
    :brief: Span over QModelRoleData objects
    :digest: dd46ae4a5bf84b77faee48d4c53b82b7

The :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` class provides a span over :sip:ref:`~PyQt6.QtCore.QModelRoleData` objects.

A :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` is used as an abstraction over an array of :sip:ref:`~PyQt6.QtCore.QModelRoleData` objects.

Like a view, :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` provides a small object (pointer and size) that can be passed to functions that need to examine the contents of the array. A :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` can be constructed from any array-like sequence (plain arrays, QVector, std::vector, QVarLengthArray, and so on). Moreover, it does not own the sequence, which must therefore be kept alive longer than any :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` objects referencing it.

Unlike a view, :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` is a span, so it allows for modifications to the underlying elements.

:sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan`'s main use case is making it possible for a model to return the data corresponding to different roles in one call.

In order to draw one element from a model, a view (through its delegates) will generally request multiple roles for the same index by calling ``data()`` as many times as needed:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py
    :lines: 147-150

:sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` allows a view to request the same data using just one function call.

This is achieved by having the view prepare a suitable array of :sip:ref:`~PyQt6.QtCore.QModelRoleData` objects, each initialized with the role that should be fetched. The array is then wrapped in a :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` object, which is then passed to a model's ``multiData()`` function.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py
    :lines: 154-167

Views are encouraged to store the array of :sip:ref:`~PyQt6.QtCore.QModelRoleData` objects (and, possibly, the corresponding span) and re-use it in subsequent calls to the model. This allows to reduce the memory allocations related with creating and returning :sip:ref:`~PyQt6.QtCore.QVariant` objects.

Finally, given a :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan` object, the model's responsibility is to fill in the data corresponding to each role in the span. How this is done depends on the concrete model class. Here's a sketch of a possible implementation that iterates over the span and uses ``setData()`` on each element:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py
    :lines: 171-180

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.multiData`.
