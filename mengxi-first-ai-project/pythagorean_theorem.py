from manim import *
import numpy as np

class PythagoreanTheorem(Scene):
    def construct(self):
        title = Tex(r"Pythagorean Theorem: $a^2 + b^2 = c^2$").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 定义直角三角形顶点
        A = np.array([-1.5, -1, 0])
        B = np.array([1.5, -1, 0])
        C = np.array([-1.5, 3, 0])

        triangle = Polygon(A, B, C, color=WHITE)
        self.play(Create(triangle))

        side_a = Tex("a").next_to(triangle.get_bottom(), DOWN)
        side_b = Tex("b").next_to(triangle.get_left(), LEFT)
        side_c = Tex("c").next_to(triangle.get_edge_center(RIGHT+UP), RIGHT, buff=0.2)

        self.play(FadeIn(side_a), FadeIn(side_b), FadeIn(side_c))
        self.wait(1)

        # 绘制平方正方形
        square_a = Square(side_length=3, fill_color=BLUE, fill_opacity=0.5).next_to(triangle, DOWN, buff=0)
        square_b = Square(side_length=4, fill_color=RED, fill_opacity=0.5).next_to(triangle, LEFT, buff=0)

        # 斜边正方形使用更复杂的手动对齐确保位置完美
        hypot_len = 5
        hypot_angle = np.arctan2(4, 3) + PI/2 # 相对底部旋转
        square_c = Square(side_length=5, fill_color=GREEN, fill_opacity=0.5)
        # 旋转角度使其与 BC 平行
        line_BC = Line(B, C)
        square_c.rotate(line_BC.get_angle())
        # 计算并移动到斜边中心
        square_c.move_to(line_BC.get_center() + 2.5 * line_BC.get_unit_vector() @ np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))

        self.play(Create(square_a))
        self.play(Write(Tex(r"$a^2$").move_to(square_a)))
        self.play(Create(square_b))
        self.play(Write(Tex(r"$b^2$").move_to(square_b)))
        
        self.wait(1)
        self.play(TransformFromCopy(VGroup(square_a, square_b), square_c), run_time=2)
        self.play(Write(Tex(r"$c^2$").move_to(square_c)))

        self.wait(3)
