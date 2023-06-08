from geometry import Vec2, Rect

ratio = Vec2(2.5, 3.5)
scale = 100
size = (ratio * scale).to_ints()

top_frame_size = int(size.y / 5)
side_frame_size = int(size.x / 20)
bottom_frame_size = int(size.y / 20)

gold_frame_thickness = int(size.x / 40)
inner_rect = Rect(
    Vec2(side_frame_size + gold_frame_thickness, top_frame_size + gold_frame_thickness),
    Vec2(size.x - side_frame_size - gold_frame_thickness, size.y - bottom_frame_size - gold_frame_thickness)    
)

suite_size = Vec2(size.x * 2 // 7, size.x * 2 // 7)
speed_triangle_position = Vec2(size.x / 2, size.y)
speed_triangle_size = Vec2(size.x / 4, size.y / 8)