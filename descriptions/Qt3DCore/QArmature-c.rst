.. sip:class-description::
    :status: todo
    :brief: Used to calculate skinning transform matrices and set them on shaders
    :realname: Qt3DCore::QArmature
    :digest: 6ccffcfcff3f5b20ff15d7a57951df7b

Used to calculate skinning transform matrices and set them on shaders.

The Armature component is aggregated by entities to give them the ability to calculate the palette of skinning transform matrices needed to properly render skinned meshes.

Each vertex in a skinned mesh is associated (bound) to up to 4 joints in a skeleton. For each joint affecting a vertex the mesh also provides a weight which determines the level of influence of the corresponding joint. The skinning palette used for performing the transformation of skinned vertices is provided by the Armature and is calculated from the joints contained in the referenced skeleton.

Updating the local transform of a joint results in the skinning matrices being recalculated and the skinned mesh vertices bound to that joint moving accordingly.
