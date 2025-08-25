from manim import *

config.frame_width = 9
config.frame_height = 16

class EulerLineProof(Scene):
    def construct(self):
        # Problem statement at the top
        problem_text = Text(
            "Given triangle ABC with orthocenter H.\nProve that point D lies on the Euler line.",
            font_size=24,
            line_spacing=0.7
        ).to_edge(UP, buff=0.5)
        
        # Solution steps at the bottom
        steps = [
            "Step 1: Draw triangle ABC and find orthocenter H.",
            "Step 2: Construct centroid G of triangle ABC.",
            "Step 3: Find circumcenter O of triangle ABC.",
            "Step 4: Draw the Euler line through H, G, O.",
            "Step 5: Show point D lies on the Euler line."
        ]
        step_texts = VGroup(*[Text(step, font_size=20) for step in steps])
        step_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step_texts.to_edge(DOWN, buff=0.5)
        
        # Initialize highlight rectangle
        highlight = SurroundingRectangle(step_texts[0], color=YELLOW, buff=0.1)
        gray_highlights = []
        
        # Triangle vertices
        A = np.array([-2, 2, 0])
        B = np.array([2, 2, 0])
        C = np.array([0, -2, 0])
        
        # Triangle and labels
        triangle = Polygon(A, B, C, color=WHITE)
        label_A = Text("A", font_size=24).next_to(A, UL, buff=0.2)
        label_B = Text("B", font_size=24).next_to(B, UR, buff=0.2)
        label_C = Text("C", font_size=24).next_to(C, DOWN, buff=0.2)
        
        # Step 1: Draw triangle and orthocenter H
        self.add(problem_text, step_texts, highlight)
        self.play(Create(triangle), Write(label_A), Write(label_B), Write(label_C))
        
        # Altitudes to find orthocenter
        def get_orthogonal_line(point1, point2, foot):
            dir_vec = point2 - point1
            perp_vec = np.array([-dir_vec[1], dir_vec[0], 0])
            return Line(foot, foot + 3 * perp_vec / np.linalg.norm(perp_vec))
        
        altitude_BC = get_orthogonal_line(B, C, A)
        altitude_AC = get_orthogonal_line(A, C, B)
        
        # Find orthocenter H (intersection of altitudes)
        def line_intersection(line1, line2):
            p1, p2 = line1.get_start(), line1.get_end()
            p3, p4 = line2.get_start(), line2.get_end()
            denom = (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0])
            t = ((p1[0] - p3[0]) * (p3[1] - p4[1]) - (p1[1] - p3[1]) * (p3[0] - p4[0])) / denom
            return p1 + t * (p2 - p1)
        
        H = line_intersection(altitude_BC, altitude_AC)
        label_H = Text("H", font_size=24).next_to(H, UR, buff=0.2)
        
        self.play(Create(altitude_BC), Create(altitude_AC), Write(label_H))
        dot_H = Dot(H)
        self.play(Create(dot_H))
        self.wait(1)
        
        # Fade out altitudes
        self.play(FadeOut(altitude_BC), FadeOut(altitude_AC))
        
        # Step 2: Construct centroid G
        gray_highlights.append(highlight.copy().set_color(GRAY))
        self.play(ReplacementTransform(highlight, SurroundingRectangle(step_texts[1], color=YELLOW, buff=0.1)))
        highlight = SurroundingRectangle(step_texts[1], color=YELLOW, buff=0.1)
        
        # Medians to find centroid
        mid_BC = (B + C) / 2
        mid_AC = (A + C) / 2
        median_A = Line(A, mid_BC)
        median_B = Line(B, mid_AC)
        G = line_intersection(median_A, median_B)
        label_G = Text("G", font_size=24).next_to(G, UL, buff=0.2)
        
        self.play(Create(median_A), Create(median_B), Write(label_G))
        dot_G = Dot(G)
        self.play(Create(dot_G))
        self.wait(1)
        
        # Fade out medians
        self.play(FadeOut(median_A), FadeOut(median_B))
        
        # Step 3: Find circumcenter O
        gray_highlights.append(highlight.copy().set_color(GRAY))
        self.play(ReplacementTransform(highlight, SurroundingRectangle(step_texts[2], color=YELLOW, buff=0.1)))
        highlight = SurroundingRectangle(step_texts[2], color=YELLOW, buff=0.1)
        
        # Perpendicular bisectors
        perp_bisector_BC = get_orthogonal_line(B, C, mid_BC)
        perp_bisector_AC = get_orthogonal_line(A, C, mid_AC)
        O = line_intersection(perp_bisector_BC, perp_bisector_AC)
        label_O = Text("O", font_size=24).next_to(O, DR, buff=0.2)
        
        self.play(Create(perp_bisector_BC), Create(perp_bisector_AC), Write(label_O))
        dot_O = Dot(O)
        self.play(Create(dot_O))
        self.wait(1)
        
        # Fade out perpendicular bisectors
        self.play(FadeOut(perp_bisector_BC), FadeOut(perp_bisector_AC))
        
        # Step 4: Draw Euler line
        gray_highlights.append(highlight.copy().set_color(GRAY))
        self.play(ReplacementTransform(highlight, SurroundingRectangle(step_texts[3], color=YELLOW, buff=0.1)))
        highlight = SurroundingRectangle(step_texts[3], color=YELLOW, buff=0.1)
        
        euler_line = Line(H, O).scale(2)
        self.play(Create(euler_line))
        self.wait(1)
        
        # Step 5: Show point D on Euler line
        gray_highlights.append(highlight.copy().set_color(GRAY))
        self.play(ReplacementTransform(highlight, SurroundingRectangle(step_texts[4], color=YELLOW, buff=0.1)))
        highlight = SurroundingRectangle(step_texts[4], color=YELLOW, buff=0.1)
        
        # Arbitrary point D on Euler line (e.g., midpoint of H and O)
        D = (H + O) / 2
        label_D = Text("D", font_size=24).next_to(D, LEFT, buff=0.2)
        dot_D = Dot(D)
        
        self.play(Create(dot_D), Write(label_D))
        self.wait(1)
        
        # Keep everything on screen for 3 seconds
        self.add(*gray_highlights, highlight)
        self.wait(3)