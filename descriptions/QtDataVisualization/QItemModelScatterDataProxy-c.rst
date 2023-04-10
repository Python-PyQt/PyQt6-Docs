.. sip:class-description::
    :status: todo
    :brief: Proxy class for presenting data in item models with Q3DScatter
    :digest: 2ca6c142e487ced94b36368f5efc977c

Proxy class for presenting data in item models with :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`.

:sip:ref:`~PyQt6.QtDataVisualization.QItemModelScatterDataProxy` allows you to use :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` derived models as a data source for :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`. It maps roles of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` to the XYZ-values of :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter` points.

The data is resolved asynchronously whenever the mapping or the model changes. :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.arrayReset` is emitted when the data has been resolved. However, inserts, removes, and single data item changes after the model initialization are resolved synchronously, unless the same frame also contains a change that causes the whole model to be resolved.

Mapping ignores rows and columns of the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` and treats all items equally. It requires the model to provide roles for the data items that can be mapped to X, Y, and Z-values for the scatter points.

For example, assume that you have a custom :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` for storing various measurements done on material samples, providing data for roles such as "density", "hardness", and "conductivity". You could visualize these properties on a scatter graph using this proxy:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_qtdatavisualization.py
    :lines: 75-79

If the fields of the model do not contain the data in the exact format you need, you can specify a search pattern regular expression and a replace rule for each role to get the value in a format you need. For more information how the replace using regular expressions works, see QString::replace(const :sip:ref:`~PyQt6.QtCore.QRegularExpression` &rx, const QString &after) function documentation. Note that using regular expressions has an impact on the performance, so it's more efficient to utilize item models where doing search and replace is not necessary to get the desired values.

For example about using the search patterns in conjunction with the roles, see `ItemModelBarDataProxy <https://doc.qt.io/qt-6/qml-qtdatavisualization-itemmodelbardataproxy.html>`_ usage in `Simple Bar Graph <https://doc.qt.io/qt-6/qtdatavis3d-qmlbars-example.html>`_ example.

.. seealso:: `Qt Data Visualization Data Handling <https://doc.qt.io/qt-6/qtdatavisualization-data-handling.html>`_.
