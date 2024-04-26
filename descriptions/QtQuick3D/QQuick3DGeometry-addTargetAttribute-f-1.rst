.. sip:method-description::
    :status: todo
    :pysig: 0343d2aec7159670c2ea8b3d873d9897
    :realsig: (quint32, QQuick3DGeometry::Attribute::Semantic, int, int)
    :digest: dc9870540f718e27eb8e4ec1cbf7df7f

Adds morph target attribute description. Each attribute has a *targetId* which the attribute belongs to, a *semantic*, which specifies the usage of the attribute and the number of components it has, an *offset* from the beginning to the vertex to the attribute location inside a vertex, and a *stride* which is a byte size between the elements.

**Note:** The targetId should be increased from 0 without skipping any number and all the targets should have the same attributes.

**Note:** The semantic is the same as the vertex attribute but IndexSemantic, JointSementic and WeightSemantic are not allowed for target attributes.

**Note:** The componentTypes of all the target attributes must be F32Type.

**Note:** If the stride is not given or less than or equal to zero, the attribute is considered to be tightly packed.

.. seealso:: :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry.addAttribute`.
