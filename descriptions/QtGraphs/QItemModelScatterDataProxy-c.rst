.. sip:class-description::
    :status: todo
    :brief: Proxy class for presenting data in item models with Q3DScatterWidgetItem
    :digest: 368ace88118e63099d450739599bed12

Proxy class for presenting data in item models with :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DScatterWidgetItem`.

:sip:ref:`~PyQt6.QtGraphs.QItemModelScatterDataProxy` allows you to use :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` derived models as a data source for :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DScatterWidgetItem`. It maps roles of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` to the XYZ-values of :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DScatterWidgetItem` points.

The data is resolved asynchronously whenever the mapping or the model changes. :sip:ref:`~PyQt6.QtGraphs.QScatterDataProxy.arrayReset` is emitted when the data has been resolved. However, inserts, removes, and single data item changes after the model initialization are resolved synchronously, unless the same frame also contains a change that causes the whole model to be resolved.

Mapping ignores rows and columns of the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` and treats all items equally. It requires the model to provide roles for the data items that can be mapped to X, Y, and Z-values for the scatter points.

For example, assume that you have a custom :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` for storing various measurements done on material samples, providing data for roles such as "density", "hardness", and "conductivity". You could visualize these properties on a scatter graph using this proxy:

.. literalinclude:: ../../../snippets/qtgraphs-src-doc-snippets-doc_src_qtgraphs.py
    :lines: 45-49

If the fields of the model do not contain the data in the exact format you need, you can specify a search pattern regular expression and a replace rule for each role to get the value in a format you need. For more information on how the replacement using regular expressions works, see the QString::replace(const :sip:ref:`~PyQt6.QtCore.QRegularExpression` &rx, const QString &after) function documentation. Note that using regular expressions has an impact on performance, so it's more efficient to utilize item models where doing search and replace is not necessary to get the desired values.

For example about using the search patterns in conjunction with the roles, see `ItemModelBarDataProxy <https://doc.qt.io/qt-6/qml-qtgraphs-itemmodelbardataproxy.html>`_ usage in `Simple Bar Graph <https://doc.qt.io/qt-6/qtgraphs-3d-bars-example.html>`_.

.. seealso:: `Qt Graphs Data Handling with 3D <https://doc.qt.io/qt-6/qtgraphs-data-handling.html>`_.
