from manim import *

class EulerLineShort(Scene):
    def construct(self):
        # ===== HEADER (ĐỀ BÀI) =====
        problem_text = Text(
            "Bài toán: Cho tam giác ABC có trực tâm H.\n"
            "Chứng minh rằng điểm D thuộc đường thẳng Euler.",
            font_size=34,
            color=WHITE
        ).to_edge(UP)

        # ===== FOOTER (LỜI GIẢI) =====
        steps = [
            "B1: Vẽ tam giác ABC.",
            "B2: Xác định trực tâm H.",
            "B3: Tìm trọng tâm G.",
            "B4: Xác định điểm D đặc biệt.",
            "B5: Vẽ đường Euler qua G, H, O."
        ]
        step_texts = VGroup(*[
            Text(step, font_size=28, color=GRAY)
            for step in steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN)

        # Highlight box (di chuyển qua từng bước)
        highlight_box = SurroundingRectangle(step_texts[0], color=YELLOW, buff=0.15)

        # ===== MAIN (HÌNH VẼ) =====
        A = UP*2
        B = LEFT*2 + DOWN
        C = RIGHT*2 + DOWN
        triangle = Polygon(A, B, C, color=WHITE)

        # Trọng tâm G
        G = (A + B + C) / 3
        G_dot = Dot(G, color=ORANGE)
        G_label = Text("G", font_size=24).next_to(G_dot, RIGHT)

        # Trực tâm H (lấy xấp xỉ giữa tam giác)
        H = triangle.get_center() + DOWN*0.3
        H_dot = Dot(H, color=YELLOW)
        H_label = Text("H", font_size=24).next_to(H_dot, RIGHT)

        # Tâm ngoại tiếp O (lấy trung điểm BC cho đơn giản)
        O = (B + C) / 2
        O_dot = Dot(O, color=BLUE)
        O_label = Text("O", font_size=24).next_to(O_dot, DOWN)

        # Điểm D (giả sử trên AH)
        D = (2*A + H) / 3
        D_dot = Dot(D, color=GREEN)
        D_label = Text("D", font_size=24).next_to(D_dot, LEFT)

        # Euler line (qua O, G, H)
        euler_line = Line(O, H, color=RED)

        # ===== ANIMATION FLOW =====
        self.play(Write(problem_text))
        self.wait(1)

        # Step 1
        self.play(Create(triangle))
        self.play(Create(highlight_box))
        self.wait(1)

        # Step 2
        self.play(
            Transform(highlight_box, SurroundingRectangle(step_texts[1], color=YELLOW, buff=0.15)),
            FadeIn(H_dot), Write(H_label)
        )
        self.wait(1)

        # Step 3
        self.play(
            Transform(highlight_box, SurroundingRectangle(step_texts[2], color=YELLOW, buff=0.15)),
            FadeIn(G_dot), Write(G_label)
        )
        self.wait(1)

        # Step 4
        self.play(
            Transform(highlight_box, SurroundingRectangle(step_texts[3], color=YELLOW, buff=0.15)),
            FadeIn(D_dot), Write(D_label)
        )
        self.wait(1)

        # Step 5
        self.play(
            Transform(highlight_box, SurroundingRectangle(step_texts[4], color=YELLOW, buff=0.15)),
            FadeIn(O_dot), Write(O_label),
            Create(euler_line)
        )
        self.wait(2)

        # Giữ nguyên layout
        self.wait(3)
