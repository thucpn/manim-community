from manim import *

class EulerLineStepByStep(Scene):
    def construct(self):
        # === BƯỚC 1: GIỚI THIỆU BÀI TOÁN ===
        intro = VGroup(
            Text("Bài toán:", font="DejaVu Sans", weight=BOLD),
            Text("Tam giác ABC có trực tâm H.", font="DejaVu Sans"),
            Text("M, N, P lần lượt là trung điểm BC, AC, AB.", font="DejaVu Sans"),
            Text("D thuộc AH sao cho AD:DH = 2:1.", font="DejaVu Sans"),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.6).to_edge(UP)

        self.play(Write(intro))
        self.wait(3)

        # === BƯỚC 2: VẼ TAM GIÁC VÀ CÁC YẾU TỐ ===
        A = np.array([-3, 2, 0])
        B = np.array([-4, -2, 0])
        C = np.array([2, -2, 0])

        triangle = Polygon(A, B, C, color=WHITE)
        labelA = Tex("A").next_to(A, UP)
        labelB = Tex("B").next_to(B, LEFT)
        labelC = Tex("C").next_to(C, RIGHT)

        self.play(Create(triangle), Write(labelA), Write(labelB), Write(labelC))
        self.wait(2)

        # === BƯỚC 3: THÊM TRỰC TÂM H (giả sử đã biết vị trí) ===
        H = np.array([-1, -1, 0])
        dotH = Dot(H, color=RED)
        labelH = Tex("H", color=RED).next_to(H, DOWN)
        self.play(FadeIn(dotH), Write(labelH))
        self.wait(2)

        # === BƯỚC 4: TRUNG ĐIỂM M, N, P ===
        M = (B + C) / 2
        N = (A + C) / 2
        P = (A + B) / 2
        dots = VGroup(Dot(M), Dot(N), Dot(P))
        labels = VGroup(Tex("M").next_to(M, DOWN), Tex("N").next_to(N, RIGHT), Tex("P").next_to(P, LEFT))
        self.play(FadeIn(dots), Write(labels))
        self.wait(2)

        # === BƯỚC 5: ĐIỂM D TRÊN AH SAO CHO AD:DH=2:1 ===
        D = (2*H + A) / 3
        dotD = Dot(D, color=YELLOW)
        labelD = Tex("D", color=YELLOW).next_to(D, RIGHT)
        self.play(FadeIn(dotD), Write(labelD))
        self.wait(2)

        # Chú giải step 1
        explain1 = Text("Bước 1: Xác định D trên AH sao cho AD:DH = 2:1.", font="DejaVu Sans").scale(0.5).to_edge(DOWN)
        self.play(Write(explain1))
        self.wait(3)
        self.play(FadeOut(explain1))

        # === BƯỚC 6: HIỂN THỊ ĐƯỜNG EULER ===
        centroid = (A + B + C) / 3
        O = (A + B + C) / 3  # tạm vẽ gần centroid
        euler_line = DashedLine(A, H, color=BLUE)
        self.play(Create(euler_line))
        self.wait(2)

        explain2 = Text("Bước 2: Đường Euler đi qua trực tâm H, trọng tâm G và tâm O.", font="DejaVu Sans").scale(0.5).to_edge(DOWN)
        self.play(Write(explain2))
        self.wait(3)
        self.play(FadeOut(explain2))

        # Highlight D nằm trên Euler line
        circleD = Circle(radius=0.3, color=YELLOW).move_to(D)
        self.play(Create(circleD))
        self.wait(2)

        explain3 = Text("=> D nằm trên đường Euler của tam giác.", font="DejaVu Sans").scale(0.5).to_edge(DOWN)
        self.play(Write(explain3))
        self.wait(3)
        self.play(FadeOut(explain3), FadeOut(circleD))

        # Có thể tiếp tục thêm step 2, step 3,... tương tự
