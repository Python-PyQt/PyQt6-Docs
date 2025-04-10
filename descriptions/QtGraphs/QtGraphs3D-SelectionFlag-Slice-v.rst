.. sip:enum-member-description::
    :status: todo
    :value: 0x08
    :digest: 4908952389135f774984ca22e7301536

Setting this mode flag indicates that the graph should take care of the slice view handling automatically. If you wish to control the slice view yourself via Q3DScene, do not set this flag. When setting this mode flag, either ``Row`` or ``Column`` must also be set, but not both. Slicing is supported by Q3DBarsWidgetItem and Q3DSurfaceWidgetItem only. When this flag is set, slice mode is entered in the following situations:

* When selection is changed explicitly via series API to a visible item

* When selection is changed by clicking on the graph

* When the selection mode changes and the selected item is visible
