.. sip:enum-member-description::
    :status: todo
    :value: 9
    :digest: 97810675feeb4e4adfe9917f32b4881e

Indicates that the widget has no background, i.e. when the widget receives paint events, the background is not automatically repainted. **Note**: Unlike , newly exposed areas are **never** filled with the background (e.g., after showing a window for the first time the user can see "through" it until the application processes the paint events). This flag is set or cleared by the widget's author.
