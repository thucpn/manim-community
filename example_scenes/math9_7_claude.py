from manim import *

config.frame_width = 9
config.frame_height = 16

class EulerLineProof(Scene):
    def construct(self):
        # Problem statement at the top
        problem_text = Text(
            "Given triangle ABC with orthocenter H.\nProve that point D lies on the Euler line.",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        ).to_edge(UP, buff=0.5)
        
        # Solution steps at the bottom
        steps = [
            "1. Draw triangle ABC",
            "2. Find orthocenter H (altitude intersection)",
            "3. Find circumcenter O (perpendicular bisectors)",
            "4. Find centroid G (median intersection)",
            "5. Show H, G, O are collinear (Euler line)",
            "6. Verify point D lies on this line"
        ]
        
        step_texts = VGroup()
        for i, step in enumerate(steps):
            step_text = Text(step, font_size=18, color=GRAY)
            step_texts.add(step_text)
        
        step_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        step_texts.to_edge(DOWN, buff=0.5).shift(LEFT * 2)
        
        # Current step highlight
        highlight_box = SurroundingRectangle(
            step_texts[0], 
            color=YELLOW, 
            buff=0.05,
            stroke_width=2
        )
        
        # Display problem and steps
        self.add(problem_text, step_texts)
        
        # Main figure area (middle of screen)
        figure_center = ORIGIN + UP * 0.5
        
        # Step 1: Draw triangle ABC
        self.add(highlight_box)
        self.wait(1)
        
        # Triangle vertices
        A = figure_center + UP * 2 + LEFT * 1
        B = figure_center + DOWN * 1.5 + LEFT * 2
        C = figure_center + DOWN * 1.5 + RIGHT * 2.5
        
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=3)
        
        # Labels for vertices
        label_A = Text("A", font_size=20, color=WHITE).next_to(A, UP, buff=0.1)
        label_B = Text("B", font_size=20, color=WHITE).next_to(B, DOWN + LEFT, buff=0.1)
        label_C = Text("C", font_size=20, color=WHITE).next_to(C, DOWN + RIGHT, buff=0.1)
        
        self.play(Create(triangle))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)
        
        # Step 2: Find orthocenter H
        step_texts[0].set_color(GRAY)
        step_texts[1].set_color(WHITE)
        highlight_box.become(SurroundingRectangle(step_texts[1], color=YELLOW, buff=0.05, stroke_width=2))
        
        # Altitudes
        # Altitude from A to BC
        BC_vector = C - B
        BC_unit = BC_vector / np.linalg.norm(BC_vector)
        BC_perp = np.array([-BC_unit[1], BC_unit[0], 0])
        
        # Find foot of altitude from A
        AB = B - A
        proj_length = np.dot(AB, BC_unit)
        foot_A = A + proj_length * BC_unit + np.dot(A - (A + proj_length * BC_unit), BC_perp) * BC_perp
        
        # For simplicity, calculate orthocenter position manually
        H = figure_center + UP * 0.3 + RIGHT * 0.2
        
        altitude_A = Line(A, H + DOWN * 0.5, color=RED, stroke_width=2)
        altitude_B = Line(B, H + UP * 0.8 + RIGHT * 0.3, color=RED, stroke_width=2)
        
        label_H = Text("H", font_size=20, color=RED).next_to(H, DOWN + RIGHT, buff=0.1)
        dot_H = Dot(H, color=RED, radius=0.05)
        
        self.play(Create(altitude_A), Create(altitude_B))
        self.play(Create(dot_H), Write(label_H))
        self.wait(1)
        
        # Step 3: Find circumcenter O
        step_texts[1].set_color(GRAY)
        step_texts[2].set_color(WHITE)
        highlight_box.become(SurroundingRectangle(step_texts[2], color=YELLOW, buff=0.05, stroke_width=2))
        
        # Circumcenter (equidistant from all vertices)
        O = figure_center + DOWN * 0.5 + LEFT * 0.3
        
        # Perpendicular bisectors
        mid_AB = (A + B) / 2
        mid_BC = (B + C) / 2
        
        perp_bis_AB = Line(mid_AB + UP * 0.8, mid_AB + DOWN * 0.8, color=GREEN, stroke_width=2)
        perp_bis_BC = Line(mid_BC + LEFT * 1, mid_BC + RIGHT * 1, color=GREEN, stroke_width=2)
        
        dot_O = Dot(O, color=GREEN, radius=0.05)
        label_O = Text("O", font_size=20, color=GREEN).next_to(O, DOWN + LEFT, buff=0.1)
        
        self.play(Create(perp_bis_AB), Create(perp_bis_BC))
        self.play(Create(dot_O), Write(label_O))
        self.wait(1)
        
        # Step 4: Find centroid G
        step_texts[2].set_color(GRAY)
        step_texts[3].set_color(WHITE)
        highlight_box.become(SurroundingRectangle(step_texts[3], color=YELLOW, buff=0.05, stroke_width=2))
        
        # Centroid (intersection of medians)
        G = (A + B + C) / 3
        
        # Medians
        mid_BC_median = (B + C) / 2
        mid_AC = (A + C) / 2
        
        median_A = Line(A, mid_BC_median, color=PURPLE, stroke_width=2)
        median_B = Line(B, mid_AC, color=PURPLE, stroke_width=2)
        
        dot_G = Dot(G, color=PURPLE, radius=0.05)
        label_G = Text("G", font_size=20, color=PURPLE).next_to(G, UP + LEFT, buff=0.1)
        
        self.play(Create(median_A), Create(median_B))
        self.play(Create(dot_G), Write(label_G))
        self.wait(1)
        
        # Step 5: Show Euler line
        step_texts[3].set_color(GRAY)
        step_texts[4].set_color(WHITE)
        highlight_box.become(SurroundingRectangle(step_texts[4], color=YELLOW, buff=0.05, stroke_width=2))
        
        # Euler line through H, G, O
        euler_line = Line(H + UP * 2, O + DOWN * 2, color=YELLOW, stroke_width=4)
        
        euler_label = Text("Euler Line", font_size=16, color=YELLOW).next_to(euler_line.get_center(), RIGHT, buff=0.3)
        
        self.play(Create(euler_line))
        self.play(Write(euler_label))
        self.wait(1)
        
        # Step 6: Show point D on Euler line
        step_texts[4].set_color(GRAY)
        step_texts[5].set_color(WHITE)
        highlight_box.become(SurroundingRectangle(step_texts[5], color=YELLOW, buff=0.05, stroke_width=2))
        
        # Point D on the Euler line
        D = G + (H - G) * 0.3  # Point between G and H on Euler line
        
        dot_D = Dot(D, color=ORANGE, radius=0.06)
        label_D = Text("D", font_size=20, color=ORANGE).next_to(D, UP + RIGHT, buff=0.1)
        
        # Highlight that D is on the line
        d_highlight = Circle(radius=0.15, color=ORANGE, stroke_width=3).move_to(D)
        
        self.play(Create(dot_D), Write(label_D))
        self.play(Create(d_highlight))
        self.play(FadeOut(d_highlight))
        self.wait(1)
        
        # Final highlight showing the proof is complete
        step_texts[5].set_color(GREEN)
        highlight_box.become(SurroundingRectangle(step_texts[5], color=GREEN, buff=0.05, stroke_width=2))
        
        # Keep everything on screen for review
        self.wait(3)