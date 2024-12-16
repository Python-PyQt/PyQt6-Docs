.. sip:enum-member-description::
    :status: todo
    :value: 0x08
    :digest: c2597583a03a6917dc302cda6b76db32

Setting this mode flag indicates that the graph should take care of the slice view handling automatically. If you wish to control the slice view yourself via :sip:ref:`~PyQt6.QtGraphs.Q3DScene`, do not set this flag. When setting this mode flag, either ``Row`` or ``Column`` must also be set, but not both. Slicing is supported by :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DBarsWidgetItem` and :sip:ref:`~PyQt6.QtGraphsWidgets.Q3DSurfaceWidgetItem` only. When this flag is set, slice mode is entered in the following situations:

* When selection is changed explicitly via series API to a visible item

* When selection is changed by clicking on the graph

* When the selection mode changes and the selected item is visible
