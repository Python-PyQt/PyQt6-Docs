.. sip:method-description::
    :status: todo
    :pysig: 0c234c6a5b332cd2c2b29672f008b71d
    :realsig: (QCustom3DItem*)
    :digest: 7e776cb0c3f131d62f922d350e80d3e4

Adds a :sip:ref:`~PyQt6.QtDataVisualization.QCustom3DItem` *item* to the graph. Graph takes ownership of the added item.

Returns the index to the added item if the add operation was successful, -1 if trying to add a null item, and the index of the item if trying to add an already added item.

Items are rendered in the order they have been inserted. The rendering order needs to be taken into account when having solid and transparent items.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.removeCustomItems`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.removeCustomItem`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.removeCustomItemAt`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.customItems`.
