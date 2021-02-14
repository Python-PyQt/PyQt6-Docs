.. sip:class-description::
    :status: todo
    :brief: A custom mesh loader
    :realname: Qt3DRender::QMesh
    :digest: 7791ac261c9c9c8c2f9d3cde1d230519

A custom mesh loader.

Loads mesh data from external files in a variety of formats. :sip:ref:`~PyQt6.Qt3DRender.QMesh` loads data into a single mesh.

In Qt3D 5.9, :sip:ref:`~PyQt6.Qt3DRender.QMesh` supports the following formats:

* Wavefront OBJ

* Stanford Triangle Format PLY

* STL (STereoLithography)

:sip:ref:`~PyQt6.Qt3DRender.QMesh` will also support the following format if the SDK is installed and the fbx geometry loader plugin is built and found:

* Autodesk FBX

If you wish to load an entire scene made of several objects, you should rather use the :sip:ref:`~PyQt6.Qt3DRender.QSceneLoader` instead.

.. seealso:: :sip:ref:`~PyQt6.Qt3DRender.QSceneLoader`.
