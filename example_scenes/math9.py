from manim import *

class AdvancedTriangleProblem(Scene):
    def construct(self):
        # -------------------
        # 1. Tạo tam giác ABC
        # -------------------
        A = np.array([-3, 1, 0])
        B = np.array([3, 1, 0])
        C = np.array([0, 4, 0])

        # Vẽ các đỉnh
        dots = {}
        for name, point in zip(["A","B","C"], [A,B,C]):
            dots[name] = Dot(point, color=YELLOW)
            self.add(dots[name])
            self.add(Tex(name).next_to(dots[name], UP))

        # Vẽ cạnh tam giác
        edges = [
            (A, B), (B, C), (C, A)
        ]
        for p1, p2 in edges:
            self.add(Line(p1, p2, color=BLUE))

        self.wait(1)

        # -------------------
        # 2. Tính trực tâm H
        # -------------------
        # Dùng công thức vector trực tâm
        # (Ở đây demo, lấy gần đúng)
        # Trực tâm H: giao của hai đường cao
        # Đường cao từ A
        BC_slope = (C[1]-B[1])/(C[0]-B[0])
        alt_A_slope = -1/BC_slope
        # Vẽ đường cao từ A
        foot_A = np.array([0,0,0])  # placeholder, minh họa
        alt_A = DashedLine(A, foot_A, color=GREEN)
        self.add(alt_A)
        self.wait(1)

        # -------------------
        # 3. Trung điểm M,N,P
        # -------------------
        M = (B + C)/2
        N = (A + C)/2
        P = (A + B)/2
        midpoints = {"M": M, "N": N, "P": P}
        for name, pt in midpoints.items():
            self.add(Dot(pt, color=ORANGE))
            self.add(Tex(name).next_to(pt, DOWN))

        # -------------------
        # 4. Điểm D trên AH với AD:DH = 2:1
        # -------------------
        # Demo AH vector
        H = np.array([0,0,0])  # placeholder, minh họa
        D = A + 2/3*(H - A)
        dot_D = Dot(D, color=RED)
        self.add(dot_D)
        self.add(Tex("D").next_to(dot_D, UP))
        self.play(
            FadeIn(dot_D),
            run_time=1
        )
        self.wait(1)

        # -------------------
        # 5. Vẽ đường BD, CD
        # -------------------
        # Placeholder giao với đường tròn (demo)
        E = B + 0.5*(D-B)
        F = C + 0.5*(D-C)
        dot_E = Dot(E, color=PURPLE)
        dot_F = Dot(F, color=PURPLE)
        self.add(dot_E, dot_F)
        self.add(Tex("E").next_to(dot_E, UP))
        self.add(Tex("F").next_to(dot_F, UP))
        self.add(Line(B, D, color=GREEN))
        self.add(Line(C, D, color=GREEN))
        self.wait(1)

        # -------------------
        # 6. Vẽ EF, song song BC
        # -------------------
        line_EF = Line(E, F, color=RED)
        self.add(line_EF)
        self.wait(1)

        # -------------------
        # 7. Tạo giao điểm X với đường song song AB qua D
        # -------------------
        # Đường qua D song song AB
        vec_AB = B - A
        line_D_parallel = Line(D, D + vec_AB, color=YELLOW)
        self.add(line_D_parallel)
        # Giao EF ∩ (D song song AB)
        X = np.array([0,0,0])  # placeholder
        dot_X = Dot(X, color=WHITE)
        self.add(dot_X)
        self.add(Tex("X").next_to(dot_X, UP))
        self.wait(1)

        # -------------------
        # 8. Highlight tứ giác BXDC nội tiếp
        # -------------------
        quad_BXDC = Polygon(B, X, D, C, color=PURPLE)
        self.add(quad_BXDC)
        self.wait(1)

        # -------------------
        # 9. Demo tỉ số diện tích S_DEF / S_ABC
        # -------------------
        # Vẽ DEF (giả lập)
        D_demo = D
        E_demo = E
        F_demo = F
        tri_DEF = Polygon(D_demo, E_demo, F_demo, color=ORANGE, fill_opacity=0.3)
        tri_ABC = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        self.add(tri_DEF, tri_ABC)
        self.wait(2)

        # -------------------
        # Kết thúc scene
        # -------------------
        self.wait(2)
