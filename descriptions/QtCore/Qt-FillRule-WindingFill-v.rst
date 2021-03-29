.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: f2ade11bd1097d6daa566d3507f7ce82

Specifies that the region is filled using the non zero winding rule. With this rule, we determine whether a point is inside the shape by using the following method. Draw a horizontal line from the point to a location outside the shape. Determine whether the direction of the line at each intersection point is up or down. The winding number is determined by summing the direction of each intersection. If the number is non zero, the point is inside the shape. This fill mode can also in most cases be considered as the intersection of closed shapes.
