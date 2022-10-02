.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 6ec68f4f7d8763ae9046ae528b410709

Similar to PartialUpdateBlit, but instead of using framebuffer blits, the contents of the extra framebuffer is rendered by drawing a textured quad with blending enabled. This, unlike PartialUpdateBlit, allows alpha blended content and works even when the glBlitFramebuffer is not available. Performance-wise this setting is likely to be somewhat slower than PartialUpdateBlit.
