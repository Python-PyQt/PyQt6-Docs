.. sip:attribute-description::
    :status: todo
    :digest: 24f8544a7f3dd20310aea15ce4320b71

This variable holds Enables blending..

**Note:** Changing this flag should be done with care, and is best avoided. Rather, materials should always use the QSGMaterial::Blend flag to indicate that they wish to use blending. Changing this value from false to true for a material that did not declare QSGMaterial::Blend can lead to unexpected visual results.
