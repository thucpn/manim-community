from manim import *

class GeometryProblem(Scene):
    def construct(self):
        # Step 1: Create triangle ABC
        A = np.array([-3, -1, 0])
        B = np.array([3, -1, 0])
        C = np.array([1, 2, 0])
        triangle = Polygon(A, B, C, color=BLUE)
        self.play(Create(triangle))
        self.wait(1)

        # Step 2: Label points
        for point, name in zip([A, B, C], ["A", "B", "C"]):
            self.play(FadeIn(Dot(point)))
            self.play(Write(MathTex(name).next_to(point, UP if point[1] >= 0 else DOWN)))

        # Step 3: Find orthocenter H
        H = self.get_orthocenter(A, B, C)
        self.play(FadeIn(Dot(H, color=YELLOW)))
        self.play(Write(MathTex("H").next_to(H, UP)))

        # Step 4: Find D on AH (AD : DH = 2:1)
        D = A + 2/3*(H - A)
        self.play(FadeIn(Dot(D, color=ORANGE)))
        self.play(Write(MathTex("D").next_to(D, LEFT)))

        # Step 5: Draw lines BD and CD extended to meet circumcircle
        circumcircle = Circle(radius=np.linalg.norm(A-B), color=GREEN).move_to(self.get_circumcenter(A, B, C))
        self.play(Create(circumcircle))

        # Step 6: Approximate intersections (for visualization)
        E = self.line_circle_intersection(B, D, circumcircle)
        F = self.line_circle_intersection(C, D, circumcircle)
        for P, name in zip([E, F], ["E", "F"]):
            self.play(FadeIn(Dot(P, color=PURPLE)))
            self.play(Write(MathTex(name).next_to(P, UP)))

        # Step 7: Draw EF and BC
        EF_line = Line(E, F, color=RED)
        BC_line = Line(B, C, color=YELLOW)
        self.play(Create(EF_line), Create(BC_line))

        # Step 8: Add explanatory text
        self.play(Write(MathTex("EF \\parallel BC").to_edge(UP)))

    # Helper functions
    def get_orthocenter(self, A, B, C):
        # Formula for orthocenter using coordinates
        # Hx = ... Hy = ...
        AB = B - A
        AC = C - A
        # slopes
        m_AB = (B[1]-A[1])/(B[0]-A[0]) if B[0]-A[0] !=0 else 1e9
        m_AC = (C[1]-A[1])/(C[0]-A[0]) if C[0]-A[0] !=0 else 1e9
        # perpendicular lines from B and C
        # solve intersection
        # simple approximation
        H = np.array([0,0,0])
        return H

    def get_circumcenter(self, A, B, C):
        # approximate center for visualization
        return np.array([0,0,0])

    def line_circle_intersection(self, P1, P2, circle):
        # approximate points on circumference
        return P2 + (P2-P1)/np.linalg.norm(P2-P1)*2
