from manim import *

class TriangleConfiguration(Scene):
    def construct(self):
        # Step 1: Draw triangle ABC
        a = [0, 3, 0]
        b = [-2, 0, 0]
        c = [2, 0, 0]
        triangle = Polygon(a, b, c, color=WHITE)
        self.play(Create(triangle))
        dot_a = Dot(a)
        dot_b = Dot(b)
        dot_c = Dot(c)
        label_a = Text("A").next_to(dot_a, UP)
        label_b = Text("B").next_to(dot_b, LEFT)
        label_c = Text("C").next_to(dot_c, RIGHT)
        self.play(FadeIn(dot_a, dot_b, dot_c, label_a, label_b, label_c))

        # Step 2: Add orthocenter H
        h = [0, 1.3333, 0]
        dot_h = Dot(h)
        label_h = Text("H").next_to(dot_h, RIGHT)
        self.play(FadeIn(dot_h, label_h))

        # Step 3: Add point D on AH with AD:DH = 2:1
        d = [0, 1.8889, 0]
        dot_d = Dot(d)
        label_d = Text("D").next_to(dot_d, RIGHT)
        self.play(FadeIn(dot_d, label_d))

        # Step 4: Show Euler line by adding O and G
        o = [0, 0.8333, 0]
        dot_o = Dot(o)
        label_o = Text("O").next_to(dot_o, RIGHT)
        g = [0, 1, 0]
        dot_g = Dot(g)
        label_g = Text("G").next_to(dot_g, LEFT)
        self.play(FadeIn(dot_o, label_o, dot_g, label_g))
        euler_line = Line([0, 0, 0], [0, 3, 0], color=YELLOW)
        self.play(Create(euler_line))

        # Step 5: Add midpoints M, N, P
        m = [0, 0, 0]
        n = [1, 1.5, 0]
        p = [-1, 1.5, 0]
        dot_m = Dot(m)
        dot_n = Dot(n)
        dot_p = Dot(p)
        label_m = Text("M").next_to(dot_m, DOWN)
        label_n = Text("N").next_to(dot_n, RIGHT)
        label_p = Text("P").next_to(dot_p, LEFT)
        self.play(FadeIn(dot_m, dot_n, dot_p, label_m, label_n, label_p))

        # Step 6: Draw BD and CD
        line_bd = Line(b, d)
        line_cd = Line(c, d)
        self.play(Create(line_bd), Create(line_cd))

        # Step 7: Draw circumcircle
        circum_center = o
        radius = 2.1667
        circum_circle = Circle(radius=radius, center=circum_center, color=BLUE)
        self.play(Create(circum_circle))

        # Step 8: Add E and F
        e = [0.9457, 2.7825, 0]
        f = [-0.9457, 2.7825, 0]
        dot_e = Dot(e)
        dot_f = Dot(f)
        label_e = Text("E").next_to(dot_e, UP)
        label_f = Text("F").next_to(dot_f, UP)
        self.play(FadeIn(dot_e, dot_f, label_e, label_f))

        # Step 9: Draw EF and show parallel to BC
        line_ef = Line(e, f, color=GREEN)
        self.play(Create(line_ef))
        text_parallel = Text("EF || BC", color=GREEN).to_edge(DOWN)
        self.play(Write(text_parallel))
        self.wait(1)
        self.play(FadeOut(text_parallel))

        # Step 10: Line through D parallel to AB
        line_d_par_ab = DashedLine([-2, 1.8889 - (3/2)*2, 0], [2, 1.8889 + (3/2)*2, 0], color=RED)
        self.play(Create(line_d_par_ab))

        # Step 11: Add X, intersection of EF and the line
        x = [0.5957, 2.7825, 0]
        dot_x = Dot(x)
        label_x = Text("X").next_to(dot_x, UP)
        self.play(FadeIn(dot_x, label_x))

        # Step 12: Show quadrilateral BXDC is cyclic
        quad_bxdc = Polygon(b, x, d, c, color=PURPLE)
        self.play(Create(quad_bxdc))
        text_cyclic = Text("BXDC is cyclic", color=PURPLE).to_edge(DOWN)
        self.play(Write(text_cyclic))
        self.wait(1)
        self.play(FadeOut(text_cyclic))

        # Step 13: Add K, midpoint AH
        k = [0, 2.1667, 0]
        dot_k = Dot(k)
        label_k = Text("K").next_to(dot_k, LEFT)
        self.play(FadeIn(dot_k, label_k))

        # Step 14: Show quadrilateral DEKH is parallelogram
        quad_dekh = Polygon(d, e, k, h, color=ORANGE)
        self.play(Create(quad_dekh))
        text_parallelogram = Text("DEKH is parallelogram", color=ORANGE).to_edge(DOWN)
        self.play(Write(text_parallelogram))
        self.wait(1)
        self.play(FadeOut(text_parallelogram))

        # Step 15: Note about area ratio
        text_area = Text(r"\frac{S_{DEF}}{S_{ABC}} in terms of AD, DH, BC", font_size=24).to_edge(DOWN)
        self.play(Write(text_area))
        self.wait(2)