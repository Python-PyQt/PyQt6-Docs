:orphan:

.. sip:class:: PyQt6.QtQuick.QSGNode
    :description: QtQuick/QSGNode-c.rst

    .. sip:enum:: PyQt6.QtQuick.QSGNode.DirtyState
        :description: QtQuick/QSGNode-DirtyState-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.DirtyState.DirtyGeometry
            :description: QtQuick/QSGNode-DirtyState-DirtyGeometry-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.DirtyState.DirtyMaterial
            :description: QtQuick/QSGNode-DirtyState-DirtyMaterial-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.DirtyState.DirtyMatrix
            :description: QtQuick/QSGNode-DirtyState-DirtyMatrix-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.DirtyState.DirtyNodeAdded
            :description: QtQuick/QSGNode-DirtyState-DirtyNodeAdded-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.DirtyState.DirtyNodeRemoved
            :description: QtQuick/QSGNode-DirtyState-DirtyNodeRemoved-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.DirtyState.DirtyOpacity
            :description: QtQuick/QSGNode-DirtyState-DirtyOpacity-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGNode.Flags
        :description: QtQuick/QSGNode-Flags-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.Flags.OwnedByParent
            :description: QtQuick/QSGNode-Flags-OwnedByParent-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.Flags.OwnsGeometry
            :description: QtQuick/QSGNode-Flags-OwnsGeometry-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.Flags.OwnsMaterial
            :description: QtQuick/QSGNode-Flags-OwnsMaterial-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.Flags.OwnsOpaqueMaterial
            :description: QtQuick/QSGNode-Flags-OwnsOpaqueMaterial-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.Flags.UsePreprocess
            :description: QtQuick/QSGNode-Flags-UsePreprocess-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGNode.NodeType
        :description: QtQuick/QSGNode-NodeType-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.NodeType.BasicNodeType
            :description: QtQuick/QSGNode-NodeType-BasicNodeType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.NodeType.ClipNodeType
            :description: QtQuick/QSGNode-NodeType-ClipNodeType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.NodeType.GeometryNodeType
            :description: QtQuick/QSGNode-NodeType-GeometryNodeType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.NodeType.OpacityNodeType
            :description: QtQuick/QSGNode-NodeType-OpacityNodeType-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGNode.NodeType.TransformNodeType
            :description: QtQuick/QSGNode-NodeType-TransformNodeType-v.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.__init__
        :description: QtQuick/QSGNode-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.appendChildNode
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-appendChildNode-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.childAtIndex
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-childAtIndex-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.childCount
        :returns:
            int
        :description: QtQuick/QSGNode-childCount-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.firstChild
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-firstChild-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.flags
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode.Flags`
        :description: QtQuick/QSGNode-flags-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.insertChildNodeAfter
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-insertChildNodeAfter-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.insertChildNodeBefore
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-insertChildNodeBefore-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.isSubtreeBlocked
        :returns:
            bool
        :description: QtQuick/QSGNode-isSubtreeBlocked-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.lastChild
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-lastChild-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.__len__
        :returns:
            int
        :description: QtQuick/QSGNode-__len__-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.markDirty
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode.DirtyState`
        :description: QtQuick/QSGNode-markDirty-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.nextSibling
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-nextSibling-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.parent
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-parent-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.prependChildNode
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-prependChildNode-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.preprocess
        :description: QtQuick/QSGNode-preprocess-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.previousSibling
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-previousSibling-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.removeAllChildNodes
        :description: QtQuick/QSGNode-removeAllChildNodes-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.removeChildNode
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QSGNode-removeChildNode-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.setFlag
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode.Flags`
            enabled: bool = True
        :description: QtQuick/QSGNode-setFlag-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.setFlags
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode.Flags`
            enabled: bool = True
        :description: QtQuick/QSGNode-setFlags-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGNode.type
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode.NodeType`
        :description: QtQuick/QSGNode-type-f.rst
