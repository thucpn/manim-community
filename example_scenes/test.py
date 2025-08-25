from manim import *

class PyramidVisualization(ThreeDScene):
    def construct(self):
        # Các tham số
        a = 4
        b = 3
        h = 5

        # Định nghĩa các đỉnh
        A = np.array([0, 0, 0])
        B = np.array([a, 0, 0])
        D = np.array([0, b, 0])
        C = np.array([a, b, 0])
        S = np.array([a/2, b/2, h])

        # Tạo các đỉnh dưới dạng Dot
        dots = {}
        for name, point in zip(["A","B","C","D","S"], [A,B,C,D,S]):
            dots[name] = Dot3D(point, color=YELLOW)
            self.add(dots[name])
            self.add(Tex(name).next_to(dots[name], UP))

        # Vẽ các cạnh đáy
        edges_base = [
            (A, B), (B, C), (C, D), (D, A)
        ]
        for p1, p2 in edges_base:
            self.add(Line3D(p1, p2, color=BLUE))

        # Vẽ các cạnh từ đỉnh S
        edges_side = [
            (S, A), (S, B), (S, C), (S, D)
        ]
        for p1, p2 in edges_side:
            self.add(Line3D(p1, p2, color=GREEN))

        # Vẽ đường chéo AC
        self.add(Line3D(A, C, color=RED, stroke_width=2))

        # Tạo trung điểm M của SB
        M = (S + B)/2
        dot_M = Dot3D(M, color=ORANGE)
        self.add(dot_M)
        self.add(Tex("M").next_to(dot_M, UP))

        # Vẽ mặt phẳng SCD dưới dạng Transparent Surface
        surface = Polygon(S, C, D, color=PURPLE, fill_opacity=0.2)
        self.add(surface)

        # Thêm nhãn cho mặt phẳng
        plane_label = Tex("(SCD)").move_to((S+C+D)/3 + np.array([0,0,0.3]))
        self.add(plane_label)

        # Thiết lập camera 3D
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        # Animation quay 360 độ để nhìn hình học
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(8)
        self.stop_ambient_camera_rotation()
