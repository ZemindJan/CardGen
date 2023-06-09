from geometry import Vec2, Rect

ratio = Vec2(2.5, 3.5)
scale = 100
card_size = (ratio * scale).to_ints()

top_frame_size = int(card_size.y / 5)
side_frame_size = int(card_size.x / 20)
bottom_frame_size = int(card_size.y / 20)

gold_frame_thickness = int(card_size.x / 40)
inner_rect = Rect(
    Vec2(side_frame_size + gold_frame_thickness, top_frame_size + gold_frame_thickness),
    Vec2(card_size.x - side_frame_size - gold_frame_thickness, card_size.y - bottom_frame_size - gold_frame_thickness)    
)
line_spacing = 40

suite_size = Vec2(card_size.x * 2 // 7, card_size.x * 2 // 7)
speed_triangle_position = Vec2(card_size.x / 2, card_size.y)
speed_triangle_size = Vec2(card_size.x / 4, card_size.y / 8)

icon_size = Vec2(26, 26)
icon_x_buffer = 5