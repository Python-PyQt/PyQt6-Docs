.. sip:enum-member-description::
    :status: todo
    :value: 8
    :digest: 877f1ece7e4bafd6b286c0a7b70edb87

Setting this mode flag indicates that the graph should take care of the slice view handling automatically. If you wish to control the slice view yourself via :sip:ref:`~PyQt6.QtDataVisualization.Q3DScene`, do not set this flag. When setting this mode flag, either ``SelectionRow`` or ``SelectionColumn`` must also be set, but not both. Slicing is supported by :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars` and :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface` only. When this flag is set, slice mode is entered in the following situations:

* When selection is changed explicitly via series API to a visible item

* When selection is changed by clicking on the graph

* When the selection mode changes and the selected item is visible
