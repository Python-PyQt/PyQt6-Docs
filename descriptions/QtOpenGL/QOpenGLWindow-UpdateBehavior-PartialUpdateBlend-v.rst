.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 597c4ee44ac2a98f06cdc1d15fa89ccc

Similar to , but instead of using framebuffer blits, the contents of the extra framebuffer is rendered by drawing a textured quad with blending enabled. This, unlike , allows alpha blended content and works even when the glBlitFramebuffer is not available. Performance-wise this setting is likely to be somewhat slower than .
