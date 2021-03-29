.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4b381b90ce2dc040c45416dde4349aad

Mark that the vertices in this geometry has changed and must be uploaded again.

This function only has an effect when the usage pattern for vertices is StaticData and the renderer that renders this geometry uploads the geometry into Vertex Buffer Objects (VBOs).
