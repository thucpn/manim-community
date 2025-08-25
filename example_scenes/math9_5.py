from manim import *

class MathProblemShort(Scene):
    def construct(self):
        # === HEADER: ĐỀ BÀI ===
        problem = Text(
            "Bài toán: Cho tam giác ABC có trực tâm H.\n"
            "M, N, P lần lượt là trung điểm BC, AC, AB.\n"
            "D thuộc AH sao cho AD:DH = 2:1.\n"
            "Chứng minh D nằm trên đường Euler.",
            font="DejaVu Sans", weight=BOLD
        ).scale(0.45).to_edge(UP)
        self.play(Write(problem))
        self.wait(1)

        # === FOOTER: LỜI GIẢI (sẽ update dần) ===
        solution_group = VGroup().arrange(DOWN, aligned_edge=LEFT).scale(0.4).to_edge(DOWN)

        def add_solution_line(text):
            line = Text(text, font="DejaVu Sans").scale(0.5)
            solution_group.add(line)
            solution_group.arrange(DOWN, aligned_edge=LEFT).to_edge(DOWN)
            self.play(Write(line))
            self.wait(1)

        # === MIDDLE: HÌNH VẼ ===
        A = np.array([-2, 2, 0])
        B = np.array([-3, -2, 0])
        C = np.array([2, -2, 0])
        triangle = Polygon(A, B, C, color=WHITE)
        labelA = Tex("A").next_to(A, UP)
        labelB = Tex("B").next_to(B, LEFT)
        labelC = Tex("C").next_to(C, RIGHT)

        self.play(Create(triangle), Write(labelA), Write(labelB), Write(labelC))
        add_solution_line("Bước 1: Vẽ tam giác ABC.")

        # Trực tâm H (giả sử tọa độ sẵn)
        H = np.array([-0.7, -1, 0])
        dotH = Dot(H, color=RED)
        labelH = Tex("H", color=RED).next_to(H, DOWN)
        self.play(FadeIn(dotH), Write(labelH))
        add_solution_line("Bước 2: Xác định trực tâm H của tam giác.")

        # Trung điểm
        M = (B + C) / 2
        N = (A + C) / 2
        P = (A + B) / 2
        dots = VGroup(Dot(M), Dot(N), Dot(P))
        labels = VGroup(Tex("M").next_to(M, DOWN), Tex("N").next_to(N, RIGHT), Tex("P").next_to(P, LEFT))
        self.play(FadeIn(dots), Write(labels))
        add_solution_line("Bước 3: Xác định trung điểm M, N, P.")

        # Điểm D trên AH (tỉ lệ 2:1)
        D = (2*H + A) / 3
        dotD = Dot(D, color=YELLOW)
        labelD = Tex("D", color=YELLOW).next_to(D, RIGHT)
        self.play(FadeIn(dotD), Write(labelD))
        add_solution_line("Bước 4: Lấy D trên AH sao cho AD : DH = 2 : 1.")

        # Đường Euler
        centroid = (A + B + C) / 3
        G = Dot(centroid, color=GREEN)
        labelG = Tex("G", color=GREEN).next_to(centroid, UP)
        euler_line = DashedLine(A, H, color=BLUE)
        self.play(FadeIn(G), Write(labelG), Create(euler_line))
        add_solution_line("Bước 5: Vẽ đường Euler qua A, G, H.")

        # Highlight kết quả
        circleD = Circle(radius=0.3, color=YELLOW).move_to(D)
        self.play(Create(circleD))
        add_solution_line("Kết luận: D thuộc đường Euler của tam giác.")
